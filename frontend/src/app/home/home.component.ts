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
  ngOnInit(): void {}

  convert(): void {
    this.databaseService.convert(this.link).subscribe((res) => {
      if (res['saved']) {
        this.short = res['url'];
      }
    });
  }
}