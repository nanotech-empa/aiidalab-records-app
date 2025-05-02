import ipywidgets as ipw


def get_start_widget(appbase, jupbase, notebase):
    return ipw.HTML(
        f"""
    <div align="center">
        <a href="{appbase}/interface.ipynb" target="_blank">Register data records</a>
    </div>"""
    )
