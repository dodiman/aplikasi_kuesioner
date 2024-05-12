const BASE_URL = "http://127.0.0.1:5000";

const myform_elm = document.getElementById("myform");
const tbody_elm = document.getElementById("tbody");

async function fect_data() {
    try {
        const response = await axios.get(`${BASE_URL}/mulai/kuis_api`);
        const data = response.data

        // sajikan dalam tabel
        tbody_elm.innerHTML = "";

        data.forEach(item => {
            const row = document.createElement("tr");

            const idCell = document.createElement("td");
            idCell.textContent = item.id;
            row.appendChild(idCell);

            const teksCell = document.createElement("td");
            teksCell.textContent = item.teks;
            row.appendChild(teksCell);

            const kategoriCell = document.createElement("td");
            kategoriCell.textContent = item.id_kategori;
            row.appendChild(kategoriCell);

            const aksiCell = document.createElement("td");
            aksiCell.innerHTML =  `<a onclick="proses(this, event);" data-id="${item.id}" href="">Hapus</a> | <a href="${BASE_URL}/mulai/edit_kuis/${item.id}">Edit</a>`;
            row.appendChild(aksiCell);

            tbody_elm.appendChild(row);
        });

        console.log(data);

    } catch (error) {
        console.log("terjadi kesalahan");
    }
}

fect_data();

myform_elm.addEventListener("submit", async (e) => {
    e.preventDefault();
    
    const formData = new FormData(myform_elm);

    try {
        const response = await axios.post(`${BASE_URL}/mulai/kuis_api`, formData);
        const data = response.data;

        myform_elm.reset();

        fect_data();

    } catch (error) {
        console.log("terjadi kesalahan");
    }
})

async function hapus_kuis(id) {
    try {
        const response = await axios.get(`${BASE_URL}/mulai/hapus_kuis/${id}`);
        const data = response.data;

        fect_data();
    } catch (error) {
        console.log("gagal menghapus");
    }
}

function proses(elm, e) {
    e.preventDefault();

    if (confirm("apakah anda yakin?")) {
        id = elm.getAttribute("data-id");
        hapus_kuis(id);
    }
}