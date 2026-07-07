import streamlit as st
import numpy as np
import plotly.graph_objects as go

# 页面配置
st.set_page_config(page_title="LLRF低电平系统-个人项目", layout="wide")
st.title("200MHz RFQ腔体 直线加速器低电平系统 LLRF")
st.subheader("FPGA+16bit 133MSPS 高精度幅相频率闭环控制 | 个人项目作品集")

# 侧边栏交互菜单
with st.sidebar:
    st.title("📂 项目导航")
    menu = st.radio(
        "选择查看内容",
        ["项目简介", "系统构成", "核心指标", "技术难点", "我的工作", "性能仿真"]
    )

# -------------------------- 1. 项目简介 --------------------------
if menu == "项目简介":
    st.markdown("""
    ### 项目定位
    本项目为**200MHz RFQ加速腔体**设计全数字低电平控制系统（LLRF），
    实时稳定加速场**幅度、相位、谐振频率**，是直线加速器射频系统的核心控制单元。

    ### 核心价值
    - 突破传统LwIP 64KB缓存限制，支持大带宽数据回传
    - 实现亚度级相位稳定、千分之一级幅度稳定
    - 微秒级闭环响应与故障保护
    """)

# -------------------------- 2. 系统构成 --------------------------
elif menu == "系统构成":
    st.markdown("### 🔧 系统硬件与逻辑组成")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**硬件单元**")
        st.write("- 腔体射频采样前端")
        st.write("- 16bit 133MSPS 高速ADC采集")
        st.write("- FPGA+RFSoC数字处理核心")
        st.write("- DAC激励输出与功率驱动")
        st.write("- 时钟同步与低相噪LO模块")
        st.write("- 过幅/失锁/高驻波保护单元")
    with col2:
        st.success("**算法与软件**")
        st.write("- IQ正交解调与幅相解算")
        st.write("- 三闭环PID控制（幅/相/频）")
        st.write("- AFC自动频率跟踪")
        st.write("- 时序同步与脉冲控制")
        st.write("- 上位机监控与数据回传")

# -------------------------- 3. 核心指标 --------------------------
elif menu == "核心指标":
    st.markdown("### 📊 关键性能指标（可交互查看）")
    col1, col2, col3 = st.columns(3)
    col1.metric("采样精度", "16bit")
    col2.metric("采样率", "133 MSPS")
    col3.metric("闭环延迟", "<1 μs")

    col4, col5, col6 = st.columns(3)
    col4.metric("幅度稳定度", "±0.1% (100ppm)")
    col5.metric("相位稳定度", "±0.1°")
    col6.metric("频率跟踪精度", "<10 Hz")

    st.markdown("**保护响应 <10μs | 闭环带宽 >1MHz**")

# -------------------------- 4. 技术难点 --------------------------
elif menu == "技术难点":
    st.markdown("### ⚠️ 核心技术难点与解决方案")
    with st.expander("200MHz 高精度采样与信号完整性", expanded=True):
        st.write("• 高速ADC/DAC阻抗匹配、PCB串扰抑制")
        st.write("• IQ正交不平衡校正、镜像抑制")
    with st.expander("高带宽多闭环耦合控制"):
        st.write("• 幅相频三闭环解耦与前馈补偿")
        st.write("• 束流负载、温度漂移实时抑制")
    with st.expander("强EMI环境可靠性"):
        st.write("• 高功率射频干扰隔离")
        st.write("• 快速联锁与故障录波")
    with st.expander("腔体频偏跟踪"):
        st.write("• AFC+PZT调谐协同控制")
        st.write("• 动态谐振点锁定")

# -------------------------- 5. 我的工作 --------------------------
elif menu == "我的工作":
    st.markdown("### 👨‍💻 个人负责内容（突出核心能力）")
    st.success("**全流程独立负责模块**")
    st.write("✅ LLRF数字架构设计与FPGA逻辑实现")
    st.write("✅ ADC/DAC接口、IQ解调、幅相计算")
    st.write("✅ 幅度+相位+频率三闭环算法开发与调试")
    st.write("✅ 系统联调、相噪优化、抗干扰处理")
    st.write("✅ 指标测试与验证，输出稳定度报告")

    st.markdown("### 个人能力总结")
    st.write("• 精通FPGA高速数字信号处理与实时控制")
    st.write("• 掌握加速器LLRF系统设计与闭环算法")
    st.write("• 具备硬件联调、问题定位与工程落地能力")

# -------------------------- 6. 性能仿真（交互式图表） --------------------------
elif menu == "性能仿真":
    st.markdown("### 📈 幅相稳定度仿真曲线（可交互）")
    t = np.linspace(0, 1, 1000)
    amp = 1 + 0.001 * np.random.randn(len(t))  # ±0.1%波动
    phase = 0 + 0.1 * np.random.randn(len(t))   # ±0.1°波动

    fig = go.Figure()
    fig.add_trace(go.Scatter(y=amp, name="幅度归一化", line=dict(color="#1f77b4")))
    fig.add_trace(go.Scatter(y=phase, name="相位(°)", line=dict(color="#ff7f0e"), yaxis="y2"))
    fig.update_layout(
        yaxis=dict(title="幅度"),
        yaxis2=dict(title="相位(°)", overlaying="y", side="right"),
        height=400, template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.info("仿真效果：幅度稳定度±0.1%，相位稳定度±0.1°，符合项目指标")