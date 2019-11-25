# data-comm
Data communication Project

Team:
- Anshul Ahuja (B17CS006)
- Chakshu Gupta (B17CS061)

Repo link: https://github.com/anshulahuja98/data-comm

Implementation of physical and data link layer. 
- CRC check
- Framing
- Manchester encoding

Implemented in python using socket programming.

The 2 layers of the OSI Stack implemented:
1. Physical Layer: The lowest layer of the OSI reference model is the physical layer. It is responsible for the actual physical connection between the devices. The physical layer contains information in the form of bits. It is responsible for the actual physical connection between the devices. When receiving data, this layer will get the signal received and convert it into 0s and 1s and send them to the Data Link layer, which will put the frame back together.

In our project, the data is encoded using **Manchester Encoding** before being sent over the physical layer:

![](https://media.geeksforgeeks.org/wp-content/uploads/Capture-154.png)


2. Data link layer: The data link layer is responsible for the node to node delivery of the message. The main function of this layer is to make sure data transfer is error free from one node to another, over the physical layer. When a packet arrives in a network, it is the responsibility of DLL to transmit it to the Host using its MAC address.
In our project, we have used CRC code for error correction:

**Cyclic redundancy check (CRC):** In CRC, a sequence of redundant bits, called cyclic redundancy check bits, are appended to the end of data unit so that the resulting data unit becomes exactly divisible by a second, predetermined binary number.
At the destination, the incoming data unit is divided by the same number. If at this step there is no remainder, the data unit is assumed to be correct and is therefore accepted.
A remainder indicates that the data unit has been damaged in transit and therefore must be rejected.

![image](https://user-images.githubusercontent.com/36476228/69567901-8368dd00-0fe0-11ea-986d-233c97ae48b2.png)

**Framing:** Framing is a function of the data link layer. It provides a way for a sender to transmit a set of bits that are meaningful to the receiver. Character/Byte Stuffing is used when frames consist of character. If data contains ED then, byte is stuffed into data to diffentiate it from ED.

![image](https://user-images.githubusercontent.com/36476228/69568145-16a21280-0fe1-11ea-96fa-7478f5b8b0d9.png)


### Steps to use
To run the server

```python3 server.py```

![Screenshot 2019-11-25 at 10 37 35 PM](https://user-images.githubusercontent.com/36476228/69561964-4991d980-0fd4-11ea-9ce7-611074d7bf7f.png)

To run the client

```python3 client.py```

![Screenshot 2019-11-25 at 10 37 48 PM](https://user-images.githubusercontent.com/36476228/69561963-4991d980-0fd4-11ea-81aa-99bab1cc2c96.png)
