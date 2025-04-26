import java.io.*;
import java.util.ArrayList;

interface AddressBookInterface {
    void addContact(Contact contact);
    void viewContacts();
    void editContact(String name);
    void deleteContact(String name);
    void searchContact(String name);
}

abstract class Contact implements Serializable {
    protected String name;
    protected String phoneNumber;
    protected String email;
    protected String address;

    public Contact(String name, String phoneNumber, String email, String address) {
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.email = email;
        this.address = address;
    }

    // Getters and setters
    // Add as needed
}

class PersonContact extends Contact {
    public PersonContact(String name, String phoneNumber, String email, String address) {
        super(name, phoneNumber, email, address);
    }
}

class BusinessContact extends Contact {
    private String company;

    public BusinessContact(String name, String phoneNumber, String email, String address, String company) {
        super(name, phoneNumber, email, address);
        this.company = company;
    }

    // Getter and setter for company
}

class AddressBook implements AddressBookInterface {
    private ArrayList<Contact> contacts;

    public AddressBook() {
        contacts = new ArrayList<>();
        loadContacts(); // Load contacts from file upon startup
    }

    public void addContact(Contact contact) {
        contacts.add(contact);
    }

    public void viewContacts() {
        // Implement view functionality
    }

    public void editContact(String name) {
        // Implement edit functionality
    }

    public void deleteContact(String name) {
        // Implement delete functionality
    }

    public void searchContact(String name) {
        // Implement search functionality
    }

    private void loadContacts() {
        try {
            FileInputStream fileIn = new FileInputStream("addressbook.ser");
            ObjectInputStream in = new ObjectInputStream(fileIn);
            contacts = (ArrayList<Contact>) in.readObject();
            in.close();
            fileIn.close();
        } catch (IOException | ClassNotFoundException e) {
            contacts = new ArrayList<>();
        }
    }

    public void saveContacts() {
        try {
            FileOutputStream fileOut = new FileOutputStream("addressbook.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(contacts);
            out.close();
            fileOut.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class AddressBookView {
    // Implement UI using AWT components
    // Add, view, edit, delete, search functionalities
}

public class Main {
    public static void main(String[] args) {
        AddressBook addressBook = new AddressBook();
        AddressBookView addressBookView = new AddressBookView(addressBook);
        addressBookView.display();
    }
}
