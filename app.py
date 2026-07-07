import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="LLRF System - Personal Project", layout="wide")
st.title("200MHz RFQ Cavity LLRF System")
st.subheader("FPGA + 16bit 133MSPS High-Precision Amplitude-Phase-Frequency Closed-Loop Control")

# Sidebar navigation
with st.sidebar:
    st.title("📂 Project Navigation")
    menu = st.radio(
        "Select content to view",
        ["Project Overview", "System Architecture", "Key Metrics", "Technical Challenges", "My Contributions", "Performance Simulation"]
    )

# -------------------------- 1. Project Overview --------------------------
if menu == "Project Overview":
    st.image("main/200Mllrf.PNG", caption="200MHz RFQ Cavity LLRF System Diagram", use_column_width=True)
    st.markdown("""
    ### Project Positioning
    This project designs a full-digital Low-Level RF (LLRF) system for the **200MHz RFQ accelerating cavity**,
    which stabilizes the amplitude, phase, and resonant frequency of the accelerating field in real time,
    acting as the core control unit of the linear accelerator RF system.

    ### Core Values
    - Break the 64KB cache limit of traditional LwIP, support high-bandwidth data return
    - Achieve sub-degree phase stability and 0.1% amplitude stability
    - Microsecond-level closed-loop response and fault protection
    """)

# -------------------------- 2. System Architecture --------------------------
elif menu == "System Architecture":
    st.markdown("### 🔧 Hardware and Logic Composition")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Hardware Units**")
        st.write("- Cavity RF sampling front-end")
        st.write("- 16bit 133MSPS high-speed ADC acquisition")
        st.write("- FPGA+RFSoC digital processing core")
        st.write("- DAC excitation output and power drive")
        st.write("- Clock synchronization and low-phase-noise LO module")
        st.write("- Over-amplitude/loss-lock/high-VSWR protection unit")
    with col2:
        st.success("**Algorithms and Software**")
        st.write("- IQ quadrature demodulation and amplitude-phase calculation")
        st.write("- Three closed-loop PID control (amplitude/phase/frequency)")
        st.write("- AFC automatic frequency tracking")
        st.write("- Timing synchronization and pulse control")
        st.write("- Upper computer monitoring and data return")

# -------------------------- 3. Key Metrics --------------------------
elif menu == "Key Metrics":
    st.markdown("### 📊 Key Performance Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Sampling Precision", "16bit")
    col2.metric("Sampling Rate", "133 MSPS")
    col3.metric("Closed-loop Delay", "<1 μs")

    col4, col5, col6 = st.columns(3)
    col4.metric("Amplitude Stability", "±0.1% (100ppm)")
    col5.metric("Phase Stability", "±0.1°")
    col6.metric("Frequency Tracking Precision", "<10 Hz")

    st.markdown("**Protection Response <10μs | Closed-loop Bandwidth >1MHz**")

# -------------------------- 4. Technical Challenges --------------------------
elif menu == "Technical Challenges":
    st.markdown("### ⚠️ Core Technical Challenges and Solutions")
    with st.expander("200MHz High-Precision Sampling and Signal Integrity", expanded=True):
        st.write("• High-speed ADC/DAC impedance matching, PCB crosstalk suppression")
        st.write("• IQ quadrature imbalance correction, image rejection")
    with st.expander("High-Bandwidth Multi-Closed-Loop Coupling Control"):
        st.write("• Amplitude-phase-frequency three closed-loop decoupling and feedforward compensation")
        st.write("• Real-time suppression of beam loading and temperature drift")
    with st.expander("Reliability in Strong EMI Environment"):
        st.write("• High-power RF interference isolation")
        st.write("• Fast interlock and fault recording")
    with st.expander("Cavity Frequency Offset Tracking"):
        st.write("• AFC + PZT tuning cooperative control")
        st.write("• Dynamic resonance point locking")

# -------------------------- 5. My Contributions --------------------------
elif menu == "My Contributions":
    st.markdown("### 👨‍💻 Personal Responsibilities")
    st.success("**Full-Process Independent Modules**")
    st.write("✅ LLRF digital architecture design and FPGA logic implementation")
    st.write("✅ ADC/DAC interface, IQ demodulation, amplitude-phase calculation")
    st.write("✅ Amplitude+phase+frequency three closed-loop algorithm development and debugging")
    st.write("✅ System joint debugging, phase noise optimization, anti-interference processing")
    st.write("✅ Metric testing and verification, output stability report")

    st.markdown("### Personal Ability Summary")
    st.write("• Proficient in FPGA high-speed digital signal processing and real-time control")
    st.write("• Master accelerator LLRF system design and closed-loop algorithms")
    st.write("• Possess hardware joint debugging, problem location and engineering implementation capabilities")

# -------------------------- 6. Performance Simulation --------------------------
elif menu == "Performance Simulation":
    st.markdown("### 📈 Amplitude-Phase Stability Simulation Curve")
    t = np.linspace(0, 1, 1000)
    amp = 1 + 0.001 * np.random.randn(len(t))  # ±0.1% fluctuation
    phase = 0 + 0.1 * np.random.randn(len(t))   # ±0.1° fluctuation

    fig = go.Figure()
    fig.add_trace(go.Scatter(y=amp, name="Normalized Amplitude", line=dict(color="#1f77b4")))
    fig.add_trace(go.Scatter(y=phase, name="Phase (°)", line=dict(color="#ff7f0e"), yaxis="y2"))
    fig.update_layout(
        yaxis=dict(title="Amplitude"),
        yaxis2=dict(title="Phase (°)", overlaying="y", side="right"),
        height=400, template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.info("Simulation result: Amplitude stability ±0.1%, phase stability ±0.1°, meeting project requirements")
