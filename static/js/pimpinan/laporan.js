const BASE_URL = "http://127.0.0.1:5000";

const tbody_elm = document.getElementById("tbody");
const bukti_pelaksanaan_link = document.getElementById("bukti_pelaksanaan_link");

const fetch = async () => {
    try {
        const response = await axios.get(`${BASE_URL}/mulai/kuis_api`);
        const data = response.data;

        console.log(data);
    } catch (error) {
        console.log("gagal fetch data");
    }
};


// fetch();

// console.log(tbody_elm);

bukti_pelaksanaan_link.style.display = "none";
bukti_pelaksanaan_link.addEventListener("click", (e) => {
    alert("oke")
    // console.log(e);
    // e.preventDefault();
    // console.log("oke")

    // let url = e.target.value;
    // window.open(url);
});

document.addEventListener("click", (e) => {
    // e.preventDefault();
    if (e.target.parentNode.tagName == "TD") {
        e.preventDefault();

        // console.log(e.target.href);
        window.open(e.target.href, "_blank");
    }
});