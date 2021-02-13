// Creates hamburger menu for mobile 
document.addEventListener('DOMContentLoaded', function () {
    let sidenavs = document.querySelectorAll(".sidenav");
    let sidenavsInstance = M.Sidenav.init(sidenavs, {edge: "right"});
});
// Asks for confirmation when you press delete button on reviews
function remove(){
    if(confirm("Are you sure you want to delete your review?")){
        delete_one();
    }
}    