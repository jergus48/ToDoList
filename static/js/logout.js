function LogOut() {
    let text = "You are logging out";
    if (confirm(text) == true) {
        location.replace("/logout/")
        location.reload();}
         }