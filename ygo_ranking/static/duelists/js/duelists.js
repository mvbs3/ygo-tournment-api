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
        document.getElementById('form-att_duelist').style.display = "block"
        nome = document.getElementById("nome").value=data["duelist"]["name"]
        nickname = document.getElementById("nickname").value=data["duelist"]["nickname"]
        email = document.getElementById("email").value=data["duelist"]["email"]
        cossyId = document.getElementById("cossyId").value=data["duelist"]["cossyId"]
        contact_number = document.getElementById("contact_number").value=data["duelist"]["contact_number"]
        id = document.getElementById("id").value=data["duelist_id"]
        //console.log(data)

        div_decks = document.getElementById('decks')
        //console.log(data['decks'].length)
        div_decks.innerHTML = ""
        for(i=0;i<data['decks'].length; i++){
            console.log(data['decks'][i]['fields']['deck'])
            div_decks.innerHTML += "\<form action='/duelists/update_deck/" + data['decks'][i]['id'] +"' method='POST'>\
                <div class='row'>\
                        <div class='col-md'>\
                            <input class='form-control' name='deck' type='text' value='" + data['decks'][i]['fields']['deck'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' name='ydkcode' type='text' value='" + data['decks'][i]['fields']['ydkcode'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' type='text' name='year' value='" + data['decks'][i]['fields']['year'] + "' >\
                        </div>\
                        <div class='col-md'>\
                            <input class='btn btn-lg btn-success' type='submit' value='ATUALIZAR'>\
                        </div>\
                    </form>\
                    <div class='col-md'>\
                        <a href='/duelists/delete_deck/"+ data['decks'][i]['id'] +"' class='btn btn-lg btn-danger'>EXCLUIR DECK</a>\
                    </div>\
                </div><br>"
        }
    })
}

function atualizar_duelist(){
    nome = document.getElementById("nome").value
    nickname = document.getElementById("nickname").value
    email = document.getElementById("email").value
    cossyId = document.getElementById("cossyId").value
    contact_number = document.getElementById("contact_number").value
    id = document.getElementById("id").value
   fetch('/duelists/atualizar_duelist/' + id,{
       method:"POST",
       headers: {
           'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            "name": nome,
            "nickname": nickname,
            "email": email,
            "cossyId": cossyId,
            "contact_number": contact_number
        })
   }).then(function(result){
       return result.json()
   }).then(function(data){
        if(data['status'] == "200"){
            nome = data['name'] 
            nickname = data['nickname']
            email = data['email']
            cossyId = data['cossyId']
            contact_number = data['contact_number']
            alert("Duelista atualizado com sucesso")
        }
       console.log(data)
   })
}