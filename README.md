### 📄 Project Title
AI-Generated Personal CV Page with IBM Granite

### 📝 Description
Proyek ini menggunakan model IBM Granite (Granite-3.3-8b-Instruct) untuk menghasilkan HTML dan CSS secara otomatis guna membangun sebuah halaman CV pribadi yang responsif dan modern. Proyek dijalankan melalui Google Colab dengan bantuan LangChain, Replicate, dan utilitas dari komunitas IBM Granite.

### 💻 Technologies Used
- IBM Granite 3.3 8B Instruct (via Replicate API)
- LangChain Community
- HTML & CSS
- Bootstrap
- Google Colab
- FontAwesome & Bootstrap Icons

### 🌟 Features
- Header dengan nama pengguna dan navbar responsif
- Tabel biodata diri lengkap
- Daftar riwayat pendidikan
- Bagian keterampilan dengan progress bar visual
- Desain bersih dan mobile-friendly
- Semua kode HTML dan CSS dihasilkan oleh AI berdasarkan prompt

### ⚙️ Setup Instructions
1. Pasang dependensi
`!pip install git+https://github.com/ibm-granite-community/utils \
    "langchain_community<0.3.0" \
    replicate`

2. Inisialisasi model Granite
   `from ibm_granite_community.notebook_utils import get_env_var
from langchain_community.llms import Replicate`

    `model = Replicate(
        model="ibm-granite/granite-3.3-8b-instruct",
        replicate_api_token=get_env_var('REPLICATE_API_TOKEN'),
        model_kwargs={"max_tokens": 1024, "temperature": 0.2},
    )`

4. Siapkan prompt dan contoh (few-shot)
• Gunakan fewshot_prompt() untuk memberi tahu model jenis output yang diinginkan.
• Tambahkan contoh kode CV HTML untuk referensi AI.

5. Gunakan get_answer_using_fewshot() untuk menghasilkan HTML
• Berikan konteks, pertanyaan, dan topik.
• Simpan hasil sebagai cv.html.

6. Tampilkan hasil HTML di Google Colab
   `from IPython.display import HTML, display
display(HTML(html_code))`

### 🤖 AI Support Explanation
AI digunakan dalam proyek ini untuk:
- Menghasilkan HTML dan CSS dari prompt teks, bukan ditulis manual oleh pengguna.
- Menginterpretasi permintaan pengguna seperti "buat CV dengan biodata dan keterampilan" menjadi kode siap pakai.
- Meniru format dan gaya dari contoh (few-shot) yang diberikan, meningkatkan konsistensi dan kualitas.
