function add_deck  (){

    container = document.getElementById("form-deck")

    html = "<br>  <div class='row'> <div class='col-md'> <input type='text' placeholder='deck' class='form-control' name='deck' > </div> <div class='col-md'><input type='text' placeholder='ydkcode' class='form-control' name='ydkcode' ></div> <div class='col-md'> <input type='number' placeholder='ano' class='form-control' name='year'> </div> </div>"

    container.innerHTML += html


}