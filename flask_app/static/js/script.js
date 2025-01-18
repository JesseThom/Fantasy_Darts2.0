var socket = io.connect('http://' + document.domain + ':' + location.port);
    
socket.on('update_team', function(data) {
    // Display a message or refresh the page
    alert(data.message);

    location.reload(); // Refresh the page for all users
});