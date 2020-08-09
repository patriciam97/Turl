import { Component, OnInit } from '@angular/core';
import { faGlobeEurope } from '@fortawesome/free-solid-svg-icons';
import { DatabaseService } from '../database.service';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
  constructor(private databaseService: DatabaseService) {}
  faGlobeEurope = faGlobeEurope;
  link: string = '';
  short: string = null;
  empty: boolean = null;
  invalid: boolean = null;
  ngOnInit(): void {}

  convert(): void {
    if (this.link.trim() !== '') {
      var expression = /[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)?/gi;
      var regex = new RegExp(expression);
      if (this.link.match(regex)) {
        this.databaseService.convert(this.link).subscribe((res) => {
          if (res['saved']) {
            this.short = res['url'];
            this.empty = null;
            this.invalid = null;
            this.link = null;
          }
        });
      } else {
        this.empty = null;
        this.short = null;
        this.invalid = true;
      }
    } else {
      this.empty = true;
      this.short = null;
      this.invalid = null;
    }
  }
}
