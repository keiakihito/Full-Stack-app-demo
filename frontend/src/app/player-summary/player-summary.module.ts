import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {PlayerSummaryComponent} from './player-summary.component';
import {routing} from 'app/player-summary/player-summary.routing';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatCardModule} from '@angular/material/card';
import {FlexModule} from '@angular/flex-layout';
import {MatListModule} from '@angular/material/list';
import {MatRadioModule} from '@angular/material/radio';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatSelectModule} from '@angular/material/select';
import {MatOptionModule} from '@angular/material/core';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {PlayersService} from 'app/_services/players.service';

import { MatTableModule } from '@angular/material/table';

@NgModule({
  declarations: [PlayerSummaryComponent],
  imports: [
    CommonModule,
    routing,
    MatAutocompleteModule, // For dropdown box
    MatToolbarModule,
    MatCardModule,
    FlexModule,
    MatListModule,
    MatRadioModule,
    MatIconModule,
    MatButtonModule,
    MatSelectModule,
    MatOptionModule,
    FormsModule,
    ReactiveFormsModule,
    MatTableModule,
  ],
  providers: [PlayersService],
  bootstrap: [PlayerSummaryComponent],
})
export class PlayerSummaryModule { }
