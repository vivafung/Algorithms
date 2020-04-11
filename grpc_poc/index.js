var protobuf = require("protobufjs");

protobuf.load("people.proto", function(err, root) {
    if (err)
        throw err;
 
    // Obtain a message type
    var AwesomeMessage = root.lookupType("awesomepackage.AwesomeMessage");
    // console.log(AwesomeMessage);
 
    // Exemplary payload
    var payload = { firstName: "vivatest", lastName: "fung", address: "hwgeo;ghweg", mood: "alright"};
    
    // Verify the payload if necessary (i.e. when possibly incomplete or invalid)
    //var errMsg = AwesomeMessage.verify(payload);
    //if (errMsg)
    //    throw Error(errMsg);
 
    // Create a new message
    var message = AwesomeMessage.create(payload); // or use .fromObject if conversion is necessary
    console.log("==================")
    console.log(message);

    // Encode a message to an Uint8Array (browser) or Buffer (node)
    var buffer = AwesomeMessage.encode(message).finish();
    console.log("==================")
    console.log(buffer);
    // ... do something with buffer
 
    // Decode an Uint8Array (browser) or Buffer (node) to a message
    var message = AwesomeMessage.decode(buffer);
    console.log("======== Decode the buffer ==========")
    console.log(message);
    // ... do something with message
 
    // If the application uses length-delimited buffers, there is also encodeDelimited and decodeDelimited.
 
    // Maybe convert the message back to a plain object
    var object = AwesomeMessage.toObject(message, {
       longs: String,
        enums: String,
        bytes: String
       // see ConversionOptions
    });
    console.log("==================")
    console.log(object);
});
