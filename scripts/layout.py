from modules import script_callbacks
import gradio as gr
from tqdm import tqdm
from os import path, listdir, rename, mkdir
from pathlib import Path


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as tools:
        with gr.Row(variant='compact'):
            with gr.Column(scale=1):
                with gr.Column(variant='panel'):
                    gr.HTML(value="<h4>Batch rename files</h4>")
                    with gr.Row(variant='compact'):
                        origin_rename_dir = gr.Textbox(
                            label='Origin dir', lines=1)
                    with gr.Row(variant='compact'):
                        target_rename_dir = gr.Textbox(
                            label='Target dir', lines=1)
                    with gr.Row(variant='compact'):
                        batch_rename_submit = gr.Button(
                            "Rename", variant="primary")

                    def batch_rename_files(origin_dir_path: str, target_dir_path: str):
                        if not path.isdir(origin_dir_path):
                            return
                        if not path.isdir(target_dir_path):
                            Path(target_dir_path).mkdir(0o777, True, True)

                        origin_names = listdir(origin_dir_path)
                        name_format = "%0{0}d".format(
                            len(str(len(origin_names))))
                        for i in tqdm(range(len(origin_names))):
                            suffix = Path(origin_names[i]).suffix
                            origin_name = path.join(
                                origin_dir_path, origin_names[i])
                            target_name = path.join(
                                target_dir_path, (name_format % i) + suffix)
                            rename(origin_name, target_name)
                    batch_rename_submit.click(batch_rename_files, inputs=[
                                              origin_rename_dir, target_rename_dir], outputs=[])
            with gr.Column(scale=1):
                pass
    return (tools, 'Tools', 'Tools'),


script_callbacks.on_ui_tabs(on_ui_tabs)
