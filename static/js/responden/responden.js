const BASE_URL = "http://127.0.0.1:5000";

const form_biodata_elm = document.getElementById("form_biodata");
const kotak_kuis_elm = document.getElementById("kotak_kuis");
const kotak_biodata_elm = document.getElementById("kotak_biodata");

async function jawaban_responden(mydata) {
    try {
        const response = await axios.post(`${BASE_URL}/mulai/jawaban_responden`, mydata);
        const data = response.data

        console.log("berhasil");
    } catch (error) {
        console.log("gagal menyimpan");
    }
}

async function fecth_data_kumpulan_kuis(elm) {
    try {
        const response = await axios.get(`${BASE_URL}/mulai/kumpulan_kuis`);
        const data = response.data;

        elm.reset();
        elm.style.display = "none";

        // tampilkan kuis yang akan di isi
        const judul_elm = document.createElement("h2");
        judul_elm.textContent = "Kuesioner";
        kotak_kuis_elm.appendChild(judul_elm);

        const form_elm = document.createElement("form");
        form_elm.setAttribute("method", "post");
        
        data.forEach((item) => {
            const group_elm = document.createElement("div");
            group_elm.classList.add("group");

            const teks_elm = document.createElement("p");
            teks_elm.textContent = item.teks;

            const class_kotak_pilihan = document.createElement("div");
            class_kotak_pilihan.classList.add("pilihan");

            const jawaban_benar_elm = document.createElement("input");
            jawaban_benar_elm.setAttribute("id", `benar${item.id}`);
            jawaban_benar_elm.setAttribute("name", `${item.id}`);
            jawaban_benar_elm.setAttribute("value", "Benar");
            jawaban_benar_elm.setAttribute("type", "radio");

            const label_benar_elm = document.createElement("label");
            label_benar_elm.textContent = "Benar";
            // label_benar_elm.style.display = "block";
            label_benar_elm.setAttribute("for", `benar${item.id}`);

            const jawaban_salah_elm = document.createElement("input");
            jawaban_salah_elm.setAttribute("id", `salah${item.id}`);
            jawaban_salah_elm.setAttribute("name", `${item.id}`);
            jawaban_salah_elm.setAttribute("value", "salah");
            jawaban_salah_elm.setAttribute("type", "radio");

            const label_salah_elm = document.createElement("label");
            label_salah_elm.textContent = "Salah";
            // label_salah_elm.style.display = "block";
            label_salah_elm.setAttribute("for", `salah${item.id}`);

            class_kotak_pilihan.appendChild(jawaban_benar_elm);
            class_kotak_pilihan.appendChild(label_benar_elm);
            class_kotak_pilihan.appendChild(jawaban_salah_elm);
            class_kotak_pilihan.appendChild(label_salah_elm);

            group_elm.appendChild(teks_elm);
            group_elm.appendChild(class_kotak_pilihan);

            form_elm.appendChild(group_elm);
        });


        const simpan_elm = document.createElement("button");
        // simpan_elm.style.display = "block";
        simpan_elm.textContent = "selesai";

        form_elm.appendChild(simpan_elm);

        form_elm.addEventListener("submit", (e) => {
            e.preventDefault();
            if (confirm("apakah anda yakin?")) {
                console.log("selesai menjawab");

                // kumpul semua data untuk dikirimkan ke server
                const jawaban_form = new FormData(form_elm);
                
                let obj3 = {}
                jawaban_form.entries().forEach((item, index) => {
                    obj3[item[0]] = item[1];
                });

                // let a = localStorage.getItem("biodata");

                // console.log(JSON.parse(a));

                // console.log(obj3);

                let mydata = {
                    "biodata": JSON.parse(localStorage.getItem("biodata")),
                    "jawaban": obj3,
                    "lainnya": [1, 3, 4]
                }

                // simpan jawaban
                jawaban_responden(mydata)

                // window.open(url=BASE_URL, target="_blank");
                window.location.href = `${BASE_URL}/mulai/responden`;
            }
        });

        kotak_kuis_elm.appendChild(form_elm);

    } catch (error) {
        console.log("gagal ambil data kuis");
    }
}

form_biodata_elm.addEventListener("submit", (e) => {
    e.preventDefault();
    const form_data = new FormData(form_biodata_elm);

    let biodata_obj = {};
    for (const pair of form_data.entries()) {
        biodata_obj[pair[0]] = pair[1];
    }

    // simpan ke local storage
    localStorage.setItem("biodata", JSON.stringify(biodata_obj));

    // sembunyikan kotak form input biodata
    kotak_biodata_elm.style.display = "none";

    // load pertanyaan
    fecth_data_kumpulan_kuis(form_biodata_elm);

});