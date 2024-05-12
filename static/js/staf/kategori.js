const BASE_URL = "http://127.0.0.1:5000";

tbody_elm = document.getElementById("tbody");

async function fetch_data_kategori() {
    try {
        const response = await axios.get(`${BASE_URL}/mulai/kategori_api`);
        const data = response.data;
        console.log(data);

        // sajikan data ke tabel
        tbody_elm.innerHTML = "";  // mengosongkan data

        data.forEach(function (item) {
            // Create a new row
            const row = document.createElement('tr');

            // Create cells for each column
            const idCell = document.createElement('td');
            idCell.textContent = item.id;
            row.appendChild(idCell);

            const kategoriCell = document.createElement('td');
            kategoriCell.textContent = item.kategori;
            row.appendChild(kategoriCell);

            const aksiCell = document.createElement('td');
            aksiCell.innerHTML = `<a data-id="${item.id}" id="tombol_hapus" onclick="hapus_kategori(this, event)" href="">hapus</a> | <a href="${BASE_URL}/mulai/edit_kategori/${item.id}">edit</a>`;
            row.appendChild(aksiCell);

            // Append the row to the table body
            tbody.appendChild(row);
        });


    } catch (error) {
        tbody_elm.innerHTML = "terjadi kesalahan";
        console.log("terjadi kesalahan ketika fetch data");
    }
}

fetch_data_kategori();


const form_input_kategori_elm = document.getElementById("form_input_kategori");


form_input_kategori_elm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form_input_kategori_elm);

    try {
        const response = await axios.post(`${BASE_URL}/mulai/kategori_api`, formData);
        const data = response.data;
        console.log(data);

        form_input_kategori_elm.reset();  // mereset form inputan

        fetch_data_kategori();  // memanggil ulang fungsi tampilkan data

    } catch (error) {
        console.log("tidak bisa input data kategori");
    }

});

// hapus kategori
async function hapus_kat(id) {
    try {
        const response = await axios.get(`${BASE_URL}/mulai/hapus_kategori/${id}`);
        const data = response.data;

        fetch_data_kategori();  // memanggil ulang fungsi tampilkan data
        
    } catch (error) {
        console.log("tidak dapat menghapus data");
    }
}

function hapus_kategori(elm, event) {
    event.preventDefault();

    if (confirm("apakah anda yakin?")) {    
    
        // const elm = document.getElementById("tombol_hapus");
        id = elm.getAttribute("data-id");

        hapus_kat(id);

        
        console.log(elm.getAttribute("data-id"));
    } else {
        
    }
}