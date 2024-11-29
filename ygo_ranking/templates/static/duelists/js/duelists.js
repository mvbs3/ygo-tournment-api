function add_deck  (){

    container = document.getElementById("form-deck")

    html = "<br>  <div class='row'> <div class='col-md'> <input type='text' placeholder='deck' class='form-control' name='deck' > </div> <div class='col-md'><input type='text' placeholder='ydkcode' class='form-control' name='ydkcode' ></div> <div class='col-md'> <input type='number' placeholder='ano' class='form-control' name='year'> </div> </div>"

    container.innerHTML += html


}

form_to_show = {"criar_duelista": 1, "atualizar_duelista": 2}
function show_form(form_show){
    add_duelist = document.getElementById("add-duelist")
    att_duelist = document.getElementById("att_duelist")
    console.log(form_show)
    if (form_show == "1"){
        att_duelist.style.display = "none"
        add_duelist.style.display = "block"
        
    }else if (form_show == "2"){
        add_duelist.style.display = "none"
        att_duelist.style.display = "block"
        console.log(att_duelist)
        
        
    }
    

}

function data_duelists(){
    duelist = document.getElementById("duelist_select")
    console.log("data_duelists")
}