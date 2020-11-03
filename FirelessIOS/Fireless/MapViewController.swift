//Firebase(Database)
import UIKit
import FirebaseDatabase

class MapViewController: UIViewController {
    @IBOutlet weak var firstRoom: UILabel!
    @IBOutlet weak var secondRoom: UILabel!
    var postData = [0, 0];
    var postData2 = [Int]();
    var ref: DatabaseReference!
    var databaseHandle:DatabaseHandle?
    override func viewDidLoad() {
        super.viewDidLoad()
        ref = Database.database().reference()
        // Do any additional setup after loading the view, typically from a nib.
    }
    @IBAction func back_pressed(_ sender: UIButton) {
        self.dismiss(animated: true, completion: nil)
    }
    @IBAction func button_pressed(_ sender: UIButton) {
        //ref = Database.database().reference()
        databaseHandle = ref?.child("face").observe(.childAdded, with: { (snapshot) in
            
            let post = snapshot.value as? Int
            
            if let actualPost = post {
                
                self.postData[0] = actualPost
                
                self.secondRoom.text = "\(self.postData[0])"
                
            }
            
        })
        
        databaseHandle = ref?.child("face2").observe(.childAdded, with: { (snapshot2) in
            
            let post2 = snapshot2.value as? Int
            
            if let actualPost = post2 {
                
                self.postData[1] = actualPost
                
                self.firstRoom.text = "\(self.postData[1])"
            }
        })
    }
}


