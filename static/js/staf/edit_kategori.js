BASE_URL = "http://127.0.0.1:5000";

const myform_elm = document.getElementById("myform");



// edit kategori
async function edit_kategori() {
    try {
        const response = await axios.get(`${BASE_URL}/mulai/hapus_kategori/${id}`);
        const data = response.data;

        fetch_data_kategori();  // memanggil ulang fungsi tampilkan data
        
    } catch (error) {
        console.log("tidak dapat menghapus data");
    }
}
