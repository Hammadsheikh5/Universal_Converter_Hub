import streamlit as st
import google.generativeai as genai

# Set Gemini API Key
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

def explain_conversion(value, from_unit, to_unit, result):
    """Call Gemini API to explain the conversion."""
    prompt = f"""
    Explain the conversion from {value} {from_unit} to {to_unit}.
    The result is {result}. Provide a detailed explanation in simple terms.
    """
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text


# Set page configuration
st.set_page_config(page_title="Universal Converter Hub", layout='centered')

# Title and description
st.title("🌍🔄Universal Converter Hub")
st.write("A one-stop solution for all your conversion needs! Easily switch between units like length, mass, and temperature or convert currencies with real-time rates. Fast, accurate, and hassle-free—get the right conversions instantly! 🚀")


tab1, tab2, tab3, tab4 = st.tabs(["Unit Converter", "Currency Converter" , "Number System Converter" , "ASCII Converter"])


with tab1:

    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .input-box {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            font-size: 20px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.header("Unit Converter")
    st.subheader("Convert between different units of measurement! 📏🌡️")
    # Dropdown for selecting conversion category
    category = st.selectbox("Select a category:", sorted(["Area", "Data Transfer Rate", "Digital Storage", "Energy", "Frequency", "Fuel Economy", "Length", "Mass", "Plane Angle", "Pressure", "Speed", "Temperature", "Time", "Volume"]))

    # Define unit conversion dictionaries
    # Length units dictionary
    length_units = {
        "Metre": 1,
        "Kilometre": 0.001,
        "Centimetre": 100,
        "Millimetre": 1000,
        "Micrometre": 1e6,
        "Nanometre": 1e9,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Feet": 3.28084,
        "Inch": 39.3701,
        "Nautical mile": 0.000539957
    }

    # Area units dictionary
    area_units = {
        "Square Metre": 1,
        "Square Kilometre": 1_000_000,  # 1 km² = 1,000,000 m²
        "Square Mile": 2_589_988.11,   # 1 mi² = 2,589,988.11 m²
        "Square Yard": 0.836127,        # 1 yd² = 0.836127 m²
        "Square Feet": 0.092903,        # 1 ft² = 0.092903 m²
        "Square Inch": 0.00064516,      # 1 in² = 0.00064516 m²
        "Acre": 4046.86,                # 1 acre = 4046.86 m²
        "Hectare": 10000                # 1 ha = 10,000 m²
    }

    # Temperature units dictionary 
    temperature_units = {
        "Kelvin" : "Kelvin",
        "Fahrenheit" :"Fahrenheit" ,
        "Celsius" :"Celsius"
    }

    # Frequency units dictionary
    frequency_units ={
            "Hertz (Hz)": 1,
            "Kilohertz (kHz)": 1e-3,  # 1 kHz = 1000 Hz
            "Megahertz (MHz)": 1e-6,  # 1 MHz = 1,000,000 Hz
            "Gigahertz (GHz)": 1e-9,  # 1 GHz = 1,000,000,000 Hz
    }

    # Data Transfer Rate units dictionary
    data_transfer_rate_units = {
        "Bit per second (bps)": 1,
        "Kilobit per second (Kbps)": 1e-3,    # 1 Kbps = 1,000 bps
        "Megabit per second (Mbps)": 1e-6,    # 1 Mbps = 1,000,000 bps
        "Gigabit per second (Gbps)": 1e-9,    # 1 Gbps = 1,000,000,000 bps
        "Terabit per second (Tbps)": 1e-12,   # 1 Tbps = 1,000,000,000,000 bps
        "Byte per second (Bps)": 1 / 8,       # 1 Bps = 8 bps
        "Kilobyte per second (KBps)": 1e-3 / 8,  # 1 KBps = 1,000 Bps
        "Megabyte per second (MBps)": 1e-6 / 8,  # 1 MBps = 1,000,000 Bps
        "Gigabyte per second (GBps)": 1e-9 / 8,  # 1 GBps = 1,000,000,000 Bps
        "Terabyte per second (TBps)": 1e-12 / 8, # 1 TBps = 1,000,000,000,000 Bps
    }

    # Digital Storage units dictionary
    digital_storage_units = {
        "Bit (b)": 1,
        "Byte (B)": 8,  # 1 Byte = 8 Bits
        "Kilobit (Kb)": 1e3,  # 1 Kb = 1,000 Bits
        "Kilobyte (KB)": 8e3,  # 1 KB = 8,000 Bits
        "Megabit (Mb)": 1e6,  # 1 Mb = 1,000,000 Bits
        "Megabyte (MB)": 8e6,  # 1 MB = 8,000,000 Bits
        "Gigabit (Gb)": 1e9,  # 1 Gb = 1,000,000,000 Bits
        "Gigabyte (GB)": 8e9,  # 1 GB = 8,000,000,000 Bits
        "Terabit (Tb)": 1e12,  # 1 Tb = 1,000,000,000,000 Bits
        "Terabyte (TB)": 8e12,  # 1 TB = 8,000,000,000,000 Bits
        "Petabit (Pb)": 1e15,  # 1 Pb = 1,000,000,000,000,000 Bits
        "Petabyte (PB)": 8e15,  # 1 PB = 8,000,000,000,000,000 Bits
        "Exabit (Eb)": 1e18,  # 1 Eb = 1,000,000,000,000,000,000 Bits
        "Exabyte (EB)": 8e18  # 1 EB = 8,000,000,000,000,000,000 Bits
    }

    # Energy Storage units dictionary
    energy_units = {
        "Joule (J)": 1,  
        "Kilojoule (kJ)": 1e3,  # 1 kJ = 1,000 J
        "Calorie (cal)": 4.184,  # 1 cal = 4.184 J
        "Kilocalorie (kcal)": 4184,  # 1 kcal = 4,184 J
        "Watt-hour (Wh)": 3600,  # 1 Wh = 3,600 J
        "Kilowatt-hour (kWh)": 3.6e6,  # 1 kWh = 3,600,000 J
        "Megajoule (MJ)": 1e6,  # 1 MJ = 1,000,000 J
        "Gigajoule (GJ)": 1e9,  # 1 GJ = 1,000,000,000 J
        "Electronvolt (eV)": 1.60218e-19,  # 1 eV = 1.60218 × 10⁻¹⁹ J
        "British Thermal Unit (BTU)": 1055.06,  # 1 BTU = 1,055.06 J
        "Foot-pound (ft-lb)": 1.35582,  # 1 ft-lb = 1.35582 J
        "US Therm": 1.05506e8  # 1 US Therm = 105,506,000 J

    }

    # Fuel Economy units dictionary 
    fuel_economy_units = {
        "Mile per US Gallon (mpg)": 1,  
        "Mile per Gallon (mpg)": 1.20095,  # 1 US mpg = 1.20095 UK mpg  
        "Kilometre per Liter (km/L)": 0.425144,  # 1 US mpg = 0.425144 km/L  
        "Liter per 100 Kilometers (L/100km)": 235.214  # 1 US mpg = 235.214 L/100km  
    }

    # Mass units dicionary
    mass_units = {
        "Gram (g)": 1,
        "Kilogram (kg)": 1000,  # 1 kg = 1000 g
        "Milligram (mg)": 0.001,  # 1 mg = 0.001 g
        "Microgram (µg)": 1e-6,  # 1 µg = 0.000001 g
        "Tonne (t)": 1e6,  # 1 tonne = 1,000,000 g
        "Imperial Ton (UK ton)": 1.016e6,  # 1 Imperial ton = 1,016,047 g
        "US Ton (Short ton)": 907184.74,  # 1 US ton = 907,184.74 g
        "Pound (lb)": 453.592,  # 1 lb = 453.592 g
        "Ounce (oz)": 28.3495,  # 1 oz = 28.3495 g
        "Stone (st)": 6350.29  # 1 st = 6350.29 g
    }

    # Speed units dictionary
    speed_units = {
        "Meter per Second (m/s)": 1,
        "Kilometer per Hour (km/h)": 3.6,  # 1 m/s = 3.6 km/h
        "Mile per Hour (mph)": 2.23694,  # 1 m/s = 2.23694 mph
        "Knot (kn)": 1.94384,  # 1 m/s = 1.94384 knots
        "Feet per Second (ft/s)": 3.28084  # 1 m/s = 3.28084 ft/s
    }

    # Plane Angle units dictionary
    plane_angle_units = {
        "Degree (°)": 180 / 3.14159265359,  # 1 rad ≈ 57.2958°
        "Radian (rad)": 1,  # Base unit
        "Milliradian (mrad)": 1000,  # 1 rad = 1000 mrad
        "Gradian (gon)": 200 / 3.14159265359,  # 1 rad ≈ 63.662 grad
        "Minute of Arc (')": 60 * (180 / 3.14159265359),  # 1 rad ≈ 3437.75 arcminutes
        "Second of Arc (\")": 3600 * (180 / 3.14159265359)  # 1 rad ≈ 206265 arcseconds
    }

    # Pressure units dictionary
    pressure_units = {
        "Pascal (Pa)": 1,  # Base unit
        "Bar": 1e5,  # 1 bar = 100,000 Pa
        "Atmosphere (atm)": 101325,  # 1 atm = 101,325 Pa
        "Torr (mmHg)": 133.322,  # 1 Torr = 133.322 Pa
        "Pound per Square Inch (psi)": 6894.76  # 1 psi = 6,894.76 Pa
    }

    # Time units dictionary
    time_units={
        "Second (s)": 1,  # Base unit
        "Millisecond (ms)": 1e-3,  # 1 ms = 0.001 s
        "Microsecond (µs)": 1e-6,  # 1 µs = 0.000001 s
        "Nanosecond (ns)": 1e-9,  # 1 ns = 0.000000001 s
        "Minute (min)": 60,  # 1 min = 60 s
        "Hour (h)": 3600,  # 1 h = 3600 s
        "Day (d)": 86400,  # 1 day = 86,400 s
        "Week (wk)": 604800,  # 1 week = 604,800 s
        "Month (mo)": 2.628e6,  # Approximate: 1 month = 2,628,000 s (30.44 days)
        "Year (yr)": 3.154e7,  # Approximate: 1 year = 31,540,000 s (365.25 days)
        "Decade (decade)": 3.154e8,  # 1 decade = 10 years = 315,400,000 s
        "Century (century)": 3.154e9  # 1 century = 100 years = 3,154,000,000 s
    }

    # Volume units dictionary
    volume_units={
        "Cubic Meter (m³)": 1,  # Base unit
        "Liter (L)": 1e-3,  # 1 L = 0.001 m³
        "Milliliter (mL)": 1e-6,  # 1 mL = 0.000001 m³
        "Cubic Inch (in³)": 1.6387e-5,  # 1 in³ = 0.000016387 m³
        "Cubic Foot (ft³)": 0.0283168,  # 1 ft³ = 0.0283168 m³
        "Cubic Yard (yd³)": 0.764555,  # 1 yd³ = 0.764555 m³
        "US Gallon (gal)": 0.00378541,  # 1 US gal = 0.00378541 m³
        "US Quart (qt)": 0.000946353,  # 1 US qt = 0.000946353 m³
        "US Pint (pt)": 0.000473176,  # 1 US pt = 0.000473176 m³
        "US Cup (cup)": 0.000236588,  # 1 US cup = 0.000236588 m³
        "US Legal Cup": 0.00024,  # 1 US Legal Cup = 0.00024 m³ (240 mL)
        "US Fluid Ounce (fl oz)": 2.9574e-5,  # 1 US fl oz = 0.000029574 m³
        "Imperial Gallon (UK gal)": 0.00454609,  # 1 UK gal = 0.00454609 m³
        "Imperial Pint (UK pt)": 0.000568261,  # 1 UK pt = 0.000568261 m³
        "Imperial Fluid Ounce (UK fl oz)": 2.8413e-5  # 1 UK fl oz = 0.000028413 m³
    }

    # Conversion logic for different categories
    # Length Conversion Logic
    def length_conversion(value, from_unit, to_unit):
        return value * (length_units[to_unit] / length_units[from_unit])

    # Area Conversion Logic
    def area_conversion(value, from_unit, to_unit):
        return value * (area_units[from_unit] / area_units[to_unit])

    # Temperature Conversion Logic
    def temperature_conversion(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

    # Frequency Conversio Logic
    def frequency_conversion(value, from_unit, to_unit):
        return value * (frequency_units[to_unit] / frequency_units[from_unit])

    # Data Transfer Rate Conversion Logic
    def data_transfer_rate_conversion(value, from_unit, to_unit):
        return value * (data_transfer_rate_units[to_unit] / data_transfer_rate_units[from_unit])

    # Digital Storage Conversion Logic
    def digital_storage_conversion(value, from_unit, to_unit):
        return value * (digital_storage_units[from_unit] / digital_storage_units[to_unit])

    # Energy Storage Conversion Logic
    def energy_conversion (value, from_unit, to_unit):
        return value * (energy_units[from_unit] / energy_units[to_unit])

    # Fuel Economy Conversion Logic
    def fuel_economy_conversion(value, from_unit, to_unit):
        if from_unit == "Liter per 100 Kilometers (L/100km)" and to_unit == "Kilometre per Liter (km/L)":
            return 100 / value
        elif from_unit == "Kilometre per Liter (km/L)" and to_unit == "Liter per 100 Kilometers (L/100km)":
            return 100 / value
        elif from_unit == "Mile per US Gallon (mpg)" and to_unit == "Liter per 100 Kilometers (L/100km)":
            return 235.214 / value
        elif from_unit == "Liter per 100 Kilometers (L/100km)" and to_unit == "Mile per US Gallon (mpg)":
            return 235.214 / value
        return value * (fuel_economy_units[to_unit] / fuel_economy_units[from_unit])

    # Digital Storage Conversion Logic
    def mass_conversion(value, from_unit, to_unit):
        return value * (mass_units[from_unit] / mass_units[to_unit])
    
    # Speed Conversion Logic
    def speed_converion(value, from_unit, to_unit):
        return value * (speed_units[to_unit] / speed_units[from_unit])

    # Plane Angle Conversion Logic
    def plane_angle_converion(value, from_unit, to_unit):
         return value * (plane_angle_units[to_unit] / plane_angle_units[from_unit])
    
    # Pressure Conversion Logic
    def pressure_conversion(value, from_unit, to_unit):
        return value * (pressure_units[from_unit] / pressure_units[to_unit])
      
    # Time Conversion Logic
    def time_conversion(value, from_unit, to_unit):
        return value * (time_units[from_unit] / time_units[to_unit])
    
    # Volume Conversion Logic
    def volume_conversion(value, from_unit, to_unit):
        return value * (volume_units[from_unit] / volume_units[to_unit])

    # User input section
    value = st.number_input("Enter value:", min_value=0.0, format="%.6f")

    # Logic for different categories
    if category == "Length":
        from_unit = st.selectbox("From:", list(length_units.keys()))
        to_unit = st.selectbox("To:", list(length_units.keys()))
        result = length_conversion(value, from_unit, to_unit)

    elif category == "Area":
        from_unit = st.selectbox("From:", list(area_units.keys()))
        to_unit = st.selectbox("To:", list(area_units.keys()))
        result = area_conversion(value, from_unit, to_unit)

    elif category == "Temperature":
        from_unit = st.selectbox("From:", list(temperature_units.keys()))
        to_unit = st.selectbox("To:", list(temperature_units.keys()))
        result = temperature_conversion(value, from_unit, to_unit)

    elif category == "Frequency":
        from_unit = st.selectbox("From:", list(frequency_units.keys()))
        to_unit = st.selectbox("To:", list(frequency_units.keys()))
        result = frequency_conversion(value, from_unit, to_unit)

    elif category == "Data Transfer Rate":
        from_unit = st.selectbox("From:", list(data_transfer_rate_units.keys()))
        to_unit = st.selectbox("To:", list(data_transfer_rate_units.keys()))
        result = data_transfer_rate_conversion(value, from_unit, to_unit)

    elif category == "Digital Storage":
        from_unit = st.selectbox("From:", list(digital_storage_units.keys()))
        to_unit = st.selectbox("To:", list(digital_storage_units.keys()))
        result = digital_storage_conversion(value, from_unit, to_unit)

    elif category == "Energy" :
        from_unit = st.selectbox("From:", list(energy_units.keys()))
        to_unit = st.selectbox("To:", list(energy_units.keys()))
        result = energy_conversion(value, from_unit, to_unit)

    elif category == "Fuel Economy" :
        from_unit = st.selectbox("From:", list(fuel_economy_units.keys()))
        to_unit = st.selectbox("To:", list(fuel_economy_units.keys()))
        result = fuel_economy_conversion(value, from_unit, to_unit)

    elif category == "Mass" :
        from_unit = st.selectbox("From:", list(mass_units.keys()))
        to_unit = st.selectbox("To:", list(mass_units.keys()))
        result = mass_conversion(value, from_unit, to_unit)

    elif category == "Speed" :
        from_unit = st.selectbox("From:", list(speed_units.keys()))
        to_unit = st.selectbox("To:", list(speed_units.keys()))
        result = speed_converion(value, from_unit, to_unit)

    elif category == "Plane Angle" :
        from_unit = st.selectbox("From:", list(plane_angle_units.keys()))
        to_unit = st.selectbox("To:", list(plane_angle_units.keys()))
        result = plane_angle_converion(value, from_unit, to_unit)

    elif category == "Pressure" :
        from_unit = st.selectbox("From:", list(pressure_units.keys()))
        to_unit = st.selectbox("To:", list(pressure_units.keys()))
        result = pressure_conversion(value, from_unit, to_unit)
        
    elif category == "Time" :
        from_unit = st.selectbox("From:", list(time_units.keys()))
        to_unit = st.selectbox("To:", list(time_units.keys()))
        result = time_conversion(value, from_unit, to_unit)

    elif category == "Volume":
        from_unit = st.selectbox("From:", list(volume_units.keys()))
        to_unit = st.selectbox("To:", list(volume_units.keys()))
        result = volume_conversion(value, from_unit, to_unit)


    # Display conversion result
    # Format the result: Convert to exponent notation if it has more than 6 decimal places
    if value > 0:
        if abs(result) < 1e-6 or abs(result) > 1e6:  # If result is very small or large
            formatted_result = "{:.6e}".format(result)  # Convert to scientific notation
        else:
            formatted_result = "{:.6f}".format(result)  # Keep normal format with 6 decimal places
        
        st.markdown(
            f'<div class="input-box"> {value} {from_unit} = {formatted_result} {to_unit} </div>',
            unsafe_allow_html=True
        )

        st.divider()
        # Explanation Button
        if st.button("Explain Conversion"):
            explanation = explain_conversion(value, from_unit, to_unit, result)
            st.markdown("**Conversion Explanation:**")
            st.write(explanation)


with tab2 : 
    st.header("Currency Converter")
    st.subheader("Convert currencies with real-time exchange rates! 🌎💲")
    st.write('"Currency Converter - Coming Soon!" 💱🚀')

with tab3 : 
    st.header("Number System Converter")
    st.subheader("Convert between different number systems! 🔢🔄")
    st.write('"Number System Converter - Coming Soon!" 🚀')

with tab4 : 
    st.header("ASCII Converter")
    st.subheader("Convert between ASCII and text! 📝🔄")
    st.write('"ASCII Converter - Coming Soon!" 🚀')


st.divider()
st.link_button("🔹 Created by Hammad Sheikh", "https://www.linkedin.com/in/hammad-sheikh-51294b284/")
st.divider()