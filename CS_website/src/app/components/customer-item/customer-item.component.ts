import { Component, Input} from '@angular/core';
import { Customer } from "src/app/Customer";

@Component({
  selector: 'app-customer-item',
  templateUrl: './customer-item.component.html',
  styleUrls: ['./customer-item.component.css']
})
export class CustomerItemComponent {
  @Input() Customer: Customer = {
    id : 0,
    Gender : "",
    Ever_married : "",
    Age	: 0,
    Graduated : "",
    Profession : "",
    Work_Experience: "",
    Spending_Score :"",
    Family_Size : 0,
    Var_1 : 0,
  }; 

}
