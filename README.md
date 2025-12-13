# 📈 Black-Scholes Options Pricing Dashboard

A real-time, interactive web application for pricing European options using the Black-Scholes model. Built with Python and Streamlit, this dashboard provides instant option valuations, Greeks calculations, and sensitivity analysis with live market data.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)

## ✨ Features

- **Real-Time Stock Data**: Fetch live stock prices and historical volatility from Yahoo Finance
- **Black-Scholes Pricing**: Calculate theoretical prices for call and put options
- **Greeks Calculation**: Compute Delta, Gamma, Theta, Vega, and Rho for risk management
- **Interactive Visualizations**: 
  - Option price vs. stock price curves
  - Volatility and time sensitivity heatmaps
  - Real-time parameter adjustments
- **User-Friendly Interface**: Clean, intuitive dashboard built with Streamlit
- **Export Capabilities**: Download results as CSV for further analysis

## 🚀 Demo

```bash
streamlit run app.py
```

Then navigate to `http://localhost:8501` in your browser.

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for fetching real-time data)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/options-pricing-dashboard.git
cd options-pricing-dashboard
```

### 2. Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install numpy scipy streamlit pandas yfinance plotly
```

## 📁 Project Structure

```
options-pricing-dashboard/
│
├── app.py                  # Main Streamlit application
├── black_scholes.py        # Black-Scholes model implementation
├── data_fetcher.py         # Real-time data fetching from Yahoo Finance
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
```

## 🎮 Usage

### Basic Usage

1. **Start the application:**
   ```bash
   streamlit run app.py
   ```

2. **Enter a stock ticker** (e.g., AAPL, MSFT, GOOGL) in the sidebar

3. **Click "Fetch Real-Time Data"** to get current market data

4. **Adjust parameters:**
   - Strike Price
   - Time to Expiration
   - Risk-Free Rate
   - Volatility

5. **View results** across three tabs:
   - **Pricing**: Option prices with intrinsic and time value breakdown
   - **Greeks**: Risk metrics for portfolio management
   - **Analysis**: Interactive sensitivity charts

### Example

```python
# Pricing Apple (AAPL) call option
Stock Price: $180.00
Strike Price: $185.00
Time to Expiration: 0.25 years (3 months)
Risk-Free Rate: 5%
Volatility: 25%

Result: Call Option Price = $5.23
```

## 📊 Understanding the Output

### Option Prices

- **Call Option**: Right to buy the stock at strike price
- **Put Option**: Right to sell the stock at strike price
- **Intrinsic Value**: Immediate exercise value
- **Time Value**: Premium over intrinsic value

### The Greeks

| Greek | Measures | Range |
|-------|----------|-------|
| **Delta (Δ)** | Price change per $1 stock move | -1 to 1 |
| **Gamma (Γ)** | Delta change per $1 stock move | Always positive |
| **Theta (Θ)** | Price decay per day | Usually negative |
| **Vega (ν)** | Price change per 1% volatility change | Always positive |
| **Rho (ρ)** | Price change per 1% rate change | Varies |

## 🛠️ Technical Details

### Black-Scholes Formula

**Call Option:**
```
C = S₀N(d₁) - Ke^(-rT)N(d₂)
```

**Put Option:**
```
P = Ke^(-rT)N(-d₂) - S₀N(-d₁)
```

Where:
```
d₁ = [ln(S₀/K) + (r + σ²/2)T] / (σ√T)
d₂ = d₁ - σ√T
```

### Data Sources

- **Stock Prices**: Yahoo Finance via `yfinance` library
- **Volatility**: Calculated from 1-year historical returns (annualized)
- **Risk-Free Rate**: User-defined (typically US Treasury rate)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Ideas for Contributions

- [ ] Add support for American options
- [ ] Implement Monte Carlo simulation
- [ ] Add binomial tree model
- [ ] Include dividend adjustments
- [ ] Add options chain display
- [ ] Implement portfolio Greeks
- [ ] Add implied volatility calculator
- [ ] Include options strategies (spreads, straddles, etc.)

## 📝 Requirements

```txt
numpy>=1.24.0
scipy>=1.10.0
streamlit>=1.28.0
pandas>=2.0.0
yfinance>=0.2.28
plotly>=5.17.0
```

## ⚠️ Limitations

- **European Options Only**: This model prices European-style options (exercise only at expiration)
- **No Dividends**: Current implementation assumes no dividend payments
- **Constant Volatility**: Assumes constant volatility (doesn't account for volatility smile)
- **Market Hours**: Yahoo Finance data may have delays during market hours
- **Educational Purpose**: This tool is for educational purposes and should not be used as the sole basis for trading decisions

## 📚 Resources

- [Black-Scholes Model - Wikipedia](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model)
- [Understanding Options Greeks](https://www.investopedia.com/trading/using-the-greeks-to-understand-options/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Yahoo Finance API](https://github.com/ranaroussi/yfinance)

## 🐛 Known Issues

- Volatility calculation may be inaccurate for newly listed stocks
- Ticker symbols must match Yahoo Finance format
- Some international stocks may not be available

## 🌟 Star History

If you find this project helpful, please consider giving it a star! ⭐

---

**Disclaimer**: This software is for educational purposes only. Do not use it as financial advice. Always consult with a qualified financial advisor before making investment decisions. The authors are not responsible for any financial losses incurred from using this software.
