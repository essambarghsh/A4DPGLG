# A4 Dynamic Price Grid Label Generator

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://python.org)
[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/essambarghsh/A4DPGLG/graphs/commit-activity)

> 🏷️ Generate professional Arabic price labels optimized for A4 printing with dynamic pricing and bulk processing

A lightweight Python tool that transforms CSV product data into beautifully formatted, print-ready Arabic price labels. Perfect for retail stores, markets, and businesses needing professional-looking price tags.

## ✨ Features

- 📄 **A4 Optimized**: Perfectly sized labels (21 per page) for standard A4 paper
- 🌐 **Arabic Support**: Full RTL (Right-to-Left) text rendering with Noto Kufi Arabic font
- 💰 **Smart Pricing**: Automatic handling of sale prices with strikethrough original prices
- 🚀 **Batch Processing**: Process hundreds of products from CSV in seconds
- 🎨 **Professional Design**: Clean, modern label design with customizable colors
- 📱 **Print Ready**: Optimized for home and commercial printers

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- pandas library

### Installation

1. Clone the repository:
```bash
git clone https://github.com/essambarghsh/A4DPGLG.git
cd A4DPGLG
```

2. Install dependencies:
```bash
pip install pandas
```

### Basic Usage

1. **Prepare your CSV file** with Arabic product data:
```csv
اسم الصنف,سعر البيع,السعر الاصلي
شاي أحمر فاخر,25.50,30.00
قهوة عربية,45.00,
سكر أبيض,15.75,18.00
```

2. **Generate labels**:
```bash
python generate_labels.py
```

3. **Print**: Open `price_labels.html` in your browser and print!

## 📋 CSV Format

Your CSV file should contain these columns:

| Column | Arabic Name | Description | Required |
|--------|-------------|-------------|----------|
| Product Name | اسم الصنف | Product name in Arabic | ✅ Yes |
| Selling Price | سعر البيع | Current selling price | ✅ Yes |
| Regular Price | السعر الاصلي | Original price (optional) | ❌ No |

### Example CSV Structure

```csv
اسم الصنف,سعر البيع,السعر الاصلي
منتج بسعر مخفض,19.99,25.00
منتج بسعر عادي,15.50,
منتج آخر,8.75,10.00
```

## 🛠️ Advanced Usage

### Custom Output File

```bash
python generate_labels.py --input products.csv --output custom_labels.html
```

### Programmatic Usage

```python
from generate_labels import generate_labels

# Generate labels from custom CSV
success = generate_labels(
    csv_file='my_products.csv',
    output_file='my_labels.html'
)

if success:
    print("Labels generated successfully!")
```

## 🎨 Customization

### Modify Label Design

Edit `template.html` to customize:
- **Colors**: Change the CSS `--border-size` and background colors
- **Fonts**: Update Google Fonts import for different Arabic fonts  
- **Layout**: Adjust grid dimensions and spacing
- **Branding**: Add your store logo or branding elements

### Label Layout

The default layout provides:
- **21 labels per A4 page** (3×7 grid)
- **Responsive text sizing** that adapts to content length
- **Automatic page breaks** for large datasets

## 📁 Project Structure

```
A4DPGLG/
├── generate_labels.py      # Main label generator script
├── template.html          # HTML template for labels
├── main.csv              # Sample product data
├── package.json          # Project metadata
├── README.md             # This file
└── price_labels.html     # Generated output (created after running)
```

## 🔧 API Reference

### `generate_labels(csv_file, output_file)`

Generate HTML price labels from CSV data.

**Parameters:**
- `csv_file` (str): Path to CSV file containing product data
- `output_file` (str): Output HTML file path

**Returns:**
- `bool`: True if successful, False otherwise

### `load_csv_data(csv_file)`

Load and validate CSV product data.

**Parameters:**
- `csv_file` (str): Path to CSV file

**Returns:**
- `pandas.DataFrame`: Cleaned product data or None if error

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/essambarghsh/A4DPGLG.git

# Install development dependencies
pip install pandas pytest

# Run tests
pytest tests/
```

## 📝 License

This project is licensed under the ISC License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Noto Kufi Arabic](https://fonts.google.com/noto/specimen/Noto+Kufi+Arabic) font by Google Fonts
- [pandas](https://pandas.pydata.org/) for CSV processing
- Arabic retail community for inspiration and feedback

## 📞 Support

- 🐛 **Bug Reports**: [Open an issue](https://github.com/essambarghsh/A4DPGLG/issues)
- 💡 **Feature Requests**: [Start a discussion](https://github.com/essambarghsh/A4DPGLG/discussions)
- 📖 **Documentation**: Check our [Wiki](https://github.com/essambarghsh/A4DPGLG/wiki)

## 🚀 What's Next?

- [ ] Web-based GUI interface
- [ ] Multiple label sizes and layouts
- [ ] Barcode integration
- [ ] Multi-language support
- [ ] Cloud processing API

---

<p align="center">
  Made with ❤️ for Arabic retail businesses
</p>

<p align="center">
  <a href="#a4-dynamic-price-grid-label-generator">⬆️ Back to Top</a>
</p>