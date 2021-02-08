document.addEventListener('DOMContentLoaded', function () {
    let sidenavs = document.querySelectorAll(".sidenav");
    let sidenavsInstance = M.Sidenav.init(sidenavs, {edge: "right"});
})
function remove(){
    if(confirm("Are you sure you want to delete your review?")){
        delete_one();
    }
}    