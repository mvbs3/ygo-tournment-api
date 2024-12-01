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

function data_duelist(){
    duelist = document.getElementById("duelist_select")
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_duelist = duelist.value
    data = new FormData()
    data.append("id_duelist", id_duelist)
    fetch("/duelists/update_duelist/",{
        method:"POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data
    }).then(function(result){
        return result.json()
    }).then(function(data){
        console.log(data)
    })
}