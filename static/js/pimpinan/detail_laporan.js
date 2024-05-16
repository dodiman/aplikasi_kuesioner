const tombol_cetak_elm = document.getElementById("tombol_cetak");
const iframe_elm = document.getElementById("iframe");

// iframe_elm.style.display = "none";

tombol_cetak_elm.addEventListener("click", (e) => {
    // window.print();

    iframe_elm.contentWindow.focus();
    iframe_elm.contentWindow.print();
    // console.log(iframe_elm.contentWindow.print());
    // iframe_elm.focus();
    // iframe_elm.print();
});