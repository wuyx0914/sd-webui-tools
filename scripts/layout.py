from modules import script_callbacks
import gradio as gr
from scripts.tools import setup_rename_ui, setup_delete_ext_ui


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as tools:
        with gr.Row(variant='compact'):
            with gr.Column(scale=1):
                setup_rename_ui()
            with gr.Column(scale=1):
                setup_delete_ext_ui()
    return (tools, 'Tools', 'Tools'),


script_callbacks.on_ui_tabs(on_ui_tabs)
