const BASE_URL = "http://127.0.0.1:5000";

const tbody_elm = document.getElementById("tbody");

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