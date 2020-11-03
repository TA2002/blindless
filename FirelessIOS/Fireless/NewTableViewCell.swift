//
//  NewTableViewCell.swift
//  Fireless
//
//  Created by Tarlan Askaruly on 09.03.2020.
//  Copyright © 2020 Tarlan Askaruly. All rights reserved.
//

import UIKit

class NewTableViewCell: UITableViewCell {

    @IBOutlet weak var picta: UIImageView!
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    @IBOutlet weak var namee: UILabel!
    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
