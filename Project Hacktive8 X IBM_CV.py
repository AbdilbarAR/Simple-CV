import ipywidgets as widgets
from IPython.display import display

# Header
header = widgets.HTML(value="""
<h1 style='color: black; font-family: Arial;'>CV Abdilbar Ainur Ridla</h1>
""")

# Biodata
biodata = widgets.HTML(value="""
<h2>Biodata Diri</h2>
<table style='width:100%; font-family: Arial;'>
<tr><td><b>Nama Lengkap</b></td><td>: Abdilbar Ainur Ridla</td></tr>
<tr><td><b>Tempat, Tanggal Lahir</b></td><td>: Bangkalan, 10 Februari 2004</td></tr>
<tr><td><b>Jenis Kelamin</b></td><td>: Laki - laki</td></tr>
<tr><td><b>Alamat</b></td><td>: Bangkalan</td></tr>
<tr><td><b>Nomor Telepon</b></td><td>: 085930919600</td></tr>
<tr><td><b>Email</b></td><td>: abdilbar.ar@gmail.com</td></tr>
<tr><td><b>Kewarganegaraan</b></td><td>: Indonesia</td></tr>
</table>
""")

# Education
education = widgets.HTML(value="""
<h2>Riwayat Pendidikan</h2>
<ul style='font-family: Arial;'>
<li><b>Universitas Negeri Surabaya</b> (2022 - sekarang)</li>
<li><b>SMAN 2 Bangkalan</b> (2019 - 2022)</li>
<li><b>SMPN 5 Bangkalan</b> (2017 - 2020)</li>
<li><b>SDN Mlajah 2 Bangkalan</b> (2011 - 2017)</li>
</ul>
""")

# Skills title
skills_title = widgets.HTML(value="""
<h2>Keterampilan</h2>
""")

# Skills progress bars
html_progress = widgets.IntProgress(value=90, min=0, max=100, description='HTML', bar_style='success')
css_progress = widgets.IntProgress(value=80, min=0, max=100, description='CSS', bar_style='info')
js_progress = widgets.IntProgress(value=80, min=0, max=100, description='JavaScript', bar_style='info')
php_progress = widgets.IntProgress(value=80, min=0, max=100, description='PHP', bar_style='warning')
mysql_progress = widgets.IntProgress(value=85, min=0, max=100, description='MySQL', bar_style='success')
laravel_progress = widgets.IntProgress(value=80, min=0, max=100, description='Laravel', bar_style='')

# Tampilkan semua
display(widgets.VBox([
    header,
    biodata,
    education,
    skills_title,
    html_progress,
    css_progress,
    js_progress,
    php_progress,
    mysql_progress,
    laravel_progress
]))