function copyToClipboard(event, text) {
    event.preventDefault();
    
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
  }

var csrf_token = document.cookie.match(/csrftoken=([^;]*)/)[1];

form_to_show = {"criar_duelista": 1, "atualizar_duelista": 2}
function show_form(form_show){
    show_duelist = document.getElementById("show-duelist")
    show_deck = document.getElementById("show-deck")
    att_duelist = document.getElementById("att_duelist")
    console.log(form_show)
    if (form_show == "1"){
        att_duelist.style.display = "none"

        show_duelist.style.display = "block"
        show_deck.style.display = "block"
        
    }else if (form_show == "2"){
        show_duelist.style.display = "none"
        show_deck.style.display = "none"
        
        att_duelist.style.display = "block"
        
        
    }
    

}

// a funcao está preparada para receber no fomrato form e nao por json, por isso essa funcao ta esquisita
// mas eu queria utilizar o alert e treinar js. 
function atualizar_deck(id){
    deck = document.getElementById("deck").value
    ydkcode = document.getElementById("ydkcode").value
    year = document.getElementById("year").value
   fetch('/duelists/update_deck/' + id,{
       method:"POST",
       headers: {
           'Content-Type': 'application/x-www-form-urlencoded'
       },
       body: `deck=${deck}&ydkcode=${ydkcode}&year=${year}`
   }).then(function(result){
       return result.json()
   }).then(function(data){
        if(data['status'] == "200"){
            alert("Deck atualizado com sucesso")
        }else{
            return alert("Error " + data['error'])
        }
       console.log(data)
   })
}

function atualizar_meu_duelist(id){
    console.log("eu estou entrando na function")
    nome = document.getElementById("nome").value
    nickname = document.getElementById("nickname").value
    email = document.getElementById("email").value
    cossyId = document.getElementById("cossyId").value
    contact_number = document.getElementById("contact_number").value
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
            window.location.href = '/usuarios/meu_perfil/';

        }else{
            return alert("Error "+ data['status'] + " - " + data['error'])
        }
       console.log(data)
   })
}

function add_deck(id){
    container = document.getElementById("decks") 
    template_deck={"deck": "No_Name", "ydkcode": "No_Ydkcode", "year":2025}
   fetch('/duelists/add_deck/',{
       method:"POST",
       headers: {
           'X-CSRFToken': csrf_token,
       },
       body: JSON.stringify({
           "deck": template_deck['deck'],
           "ydkcode": template_deck['ydkcode'],
           "year": template_deck['year'],
           "duelist": id
       })
       
   }).then(function(result){
       return result.json()
   }).then(function(data){
        if(data['status'] == "200"){
        alert("Deck adicionado com sucesso")
        window.location.href = '/usuarios/meu_perfil/';
        }    
   })
   
}