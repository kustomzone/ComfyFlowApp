import argparse
import os
import re
import base64
from pathlib import Path
from loguru import logger

import streamlit as st
import module.header as header

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--server_addr", type=str, default="127.0.0.1:8188")
    try:
        args = parser.parse_args()
        server_addr = args.server_addr

        header.page_header()

        st.session_state['server_addr'] = server_addr
        
        with st.container():
            st.markdown("## 📌 Welcome to ComfyFlowApp")
            st.markdown("""
                        ComfyFlowApp is an extension tool for ComfyUI. It helps convert ComfyUI workflows into web applications, making it easy for sharing with other users.

                        Workflow developers create workflows using ComfyUI by combining ComfyUI nodes and custom extension nodes. ComfyUI workflows can perform complex tasks like generating user avatars or changing product backgrounds for e-commerce. This addresses many real-world work needs. However, for regular users, building workflows can be quite complicated and time-consuming. 
                        
                        ComfyFlowApp simplifies the way workflows are shared and used. Workflow developers can easily share their workflows as webapp with others, however users don't need to worry about the inner details of the workflow. They can simply use the webapp.
            """)
            st.markdown("""
                        :point_right: Follow the repo [ComfyFlowApp](https://github.com/xingren23/ComfyFlowApp) to get the latest updates.
                        """)
            st.markdown("""
                        ### How to develop a ComfyFlowApp?
                        """)
            st.markdown("""
                        :one: Develop：develop workflow in ComfyUI, refer to [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
                        """)
            st.image('./docs/images/comfy-workflow.png', caption='ComfyUI workflow')
            st.markdown("""
                        :two: Upload：upload workflow image to ComfyFlowApp, and configure application parameters to generate WebApp application
                        """)
            st.image('./docs/images/comfy-upload-app.png', caption='Upload workflow image')
            st.markdown("""
                        :three: Preview：preview WebApp application online
                        """)
            st.image('./docs/images/comfy-workflow-app.png', caption='Preview WebApp application')
       
            st.markdown("""
                        ### Some examples
                        **👈 Select a demo from the Workflow page on the left** to see some examples of ComfyFlowApp can do!
                        """)  

    except SystemExit as e:
        logger.error(e)
        exit()
