from tqdm import tqdm
from os import path, listdir, unlink
import gradio as gr


def setup_delete_ext_ui():
    with gr.Column(variant='panel'):
        gr.HTML(value="<h4>Batch delete files by extension</h4>")
        with gr.Row(variant='compact'):
            origin_delete_dir = gr.Textbox(
                label='Delete dir', lines=1)
        with gr.Row(variant='compact'):
            target_extension = gr.Textbox(
                label='The extension of file', lines=1)
        with gr.Row(variant='compact'):
            batch_delete_submit = gr.Button(
                "Delete", variant="primary")

        def batch_delete_files(origin_delete_path: str, target_extension: str):
            if not path.isdir(origin_delete_path):
                return
            if not target_extension.startswith("."):
                target_extension = "." + target_extension

            origin_names = listdir(origin_delete_path)

            for i in tqdm(range(len(origin_names))):
                print(origin_names[i], target_extension)
                if not origin_names[i].endswith(target_extension):
                    continue
                origin_name = path.join(
                    origin_delete_path, origin_names[i])
                unlink(origin_name)
        batch_delete_submit.click(batch_delete_files, inputs=[
            origin_delete_dir, target_extension], outputs=[])
    return locals()
