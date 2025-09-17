#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import html
from pathlib import Path

def load_csv_data(csv_file):
    """Load and validate CSV data"""
    try:
        df = pd.read_csv(csv_file, encoding='utf-8')
        # Strip whitespace from column names
        df.columns = df.columns.str.strip()
        
        # Validate required columns
        required_cols = ['اسم الصنف', 'سعر البيع', 'السعر الاصلي']
        missing_cols = [col for col in required_cols if col not in df.columns]
        
        if missing_cols:
            print(f"Warning: Missing columns: {missing_cols}")
            print(f"Available columns: {list(df.columns)}")
        
        # Handle NaN values - only drop if product name or selling price is missing
        df = df.dropna(subset=['اسم الصنف', 'سعر البيع'])
        
        # Fill NaN values in السعر الاصلي with 0
        df['السعر الاصلي'] = df['السعر الاصلي'].fillna(0)
        
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

def create_label_html(product_name, selling_price, regular_price):
    """Create HTML for a single label"""
    # Escape HTML and handle Arabic text
    safe_product_name = html.escape(str(product_name))
    
    # Format prices
    selling_price_formatted = f"{float(selling_price):.2f}"
    
    # Check if regular price should be shown
    show_footer = regular_price is not None and float(regular_price) > 0
    
    if show_footer:
        regular_price_formatted = f"{float(regular_price):.2f}"
        footer_html = f'''
                        <div class="label-footer">
                            <span class="footer-right">بدلاً من</span>
                            <span class="regular-price">{regular_price_formatted}</span>
                            <span class="footer-left">جنيه</span>
                        </div>'''
    else:
        footer_html = '<div class="label-footer"></div>'
    
    return f'''
                <div class="label">
                    <div class="label-header">{safe_product_name}</div>
                    <div class="label-body">
                        <span class="body-right">فقط</span>
                        <span class="selling-price">{selling_price_formatted}</span>
                        <span class="body-left">جنيه</span>
                    </div>{footer_html}
                </div>'''

def load_template():
    """Load the HTML template"""
    try:
        with open('template.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print("Error: template.html not found!")
        return None
    except Exception as e:
        print(f"Error loading template: {e}")
        return None

def generate_pages(df, template):
    """Generate HTML pages with 21 labels each"""
    labels_per_page = 21
    total_products = len(df)
    total_pages = (total_products + labels_per_page - 1) // labels_per_page
    
    pages = []
    
    for page_num in range(total_pages):
        start_idx = page_num * labels_per_page
        end_idx = min(start_idx + labels_per_page, total_products)
        page_products = df.iloc[start_idx:end_idx]
        
        # Generate labels for this page
        labels_html = ""
        for _, row in page_products.iterrows():
            labels_html += create_label_html(
                row['اسم الصنف'],
                row['سعر البيع'],
                row['السعر الاصلي']
            )
        
        # Create page HTML
        page_html = f'''
        <div class="a4-page">
            <div class="labels" data-labels-no="21">{labels_html}
            </div>
        </div>'''
        
        pages.append(page_html)
    
    return pages, total_pages

def generate_labels(csv_file='main.csv', output_file='price_labels.html'):
    """Main function to generate price labels"""
    print("🏷️  A4 Dynamic Price Label Generator Starting...")
    
    # Load data
    df = load_csv_data(csv_file)
    if df is None:
        return False
    
    print(f"✅ Loaded {len(df)} products from CSV")
    
    # Load template
    template = load_template()
    if template is None:
        return False
    
    print("✅ Template loaded successfully")
    
    # Generate pages
    pages, total_pages = generate_pages(df, template)
    print(f"✅ Generated {total_pages} A4 pages")
    
    # Combine all pages
    all_pages_html = '\n'.join(pages)
    
    # Find and replace the a4-pages div content
    import re
    
    # Pattern to match the entire a4-pages div content
    pattern = r'(<div class="a4-pages">).*?(</div>\s*</body>)'
    
    replacement = f'\\1\n{all_pages_html}\n    \\2'
    
    final_html = re.sub(pattern, replacement, template, flags=re.DOTALL)
    
    # Save output
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"✅ Labels saved to {output_file}")
        print(f"📄 Total: {len(df)} products across {total_pages} A4 pages")
        return True
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return False

if __name__ == "__main__":
    # Run the generator
    success = generate_labels()
    
    if success:
        print("\n🎉 Price labels generated successfully!")
        print("💡 Open 'price_labels.html' in your browser to view/print")
    else:
        print("\n❌ Failed to generate labels. Check the errors above.")