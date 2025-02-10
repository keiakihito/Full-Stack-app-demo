import { Component, OnInit } from '@angular/core';
import { PlayersService } from '../_services/players.service';
import { untilDestroyed, UntilDestroy } from '@ngneat/until-destroy';

@UntilDestroy()
@Component({
  selector: 'player-summary-component',
  templateUrl: './player-summary.component.html',
  styleUrls: ['./player-summary.component.scss']
})
export class PlayerSummaryComponent implements OnInit {
  playerName: string = ''; // Holds the player name input
  playerSuggestions: any[] = []; // Holds the player name suggestions
  apiResponse: any; // Holds the API response for the player summary
  currentGameIndex: number = 0; // To track the currently selected game
  showShots: boolean = false; // To toggle shots view

  displayedColumns: string[] = [
    'date',
    'is_starter',
    'minutes',
    'points',
    'assists',
    'offensive_rebounds',
    'defensive_rebounds',
    'steals',
    'blocks',
    'defensive_fouls',
    'offensive_fouls',
    'free_throws_made',
    'free_throws_attempted'
  ];

  constructor(
    private playersService: PlayersService // Inject the PlayersService
  ) {}

  ngOnInit(): void {}

  onSearchInputChange(event: any): void {
    const inputValue = event.target.value;

    // Reset player summary and shots when typing new input
    this.apiResponse = null;
    this.showShots = false;  // Clear the shooting points when starting a new search

    if (inputValue.length >= 1) {  // Make the call after 2 or more characters
      this.playersService.getAutocompleteSuggestions(inputValue)
        .pipe(untilDestroyed(this))
        .subscribe((suggestions: any) => {
          this.playerSuggestions = suggestions;  // Store suggestions
        }, (error) => {
          console.error('Error fetching autocomplete suggestions:', error);
        });
    } else {
      this.playerSuggestions = [];  // Clear suggestions if input is too short
    }
  }


// Method to handle player selection
  onPlayerSelect(playerID: number): void {
    const selectedPlayer = this.playerSuggestions.find(player => player.id === playerID);

    if (selectedPlayer) {
      // Set the search input field with the full name
      this.playerName = selectedPlayer.name;

      // Proceed to fetch the player's summary
      this.playersService.getPlayerSummary(playerID)
        .pipe(untilDestroyed(this))
        .subscribe((data) => {
          this.apiResponse = data.apiResponse;  // Show the player summary after selection
          this.showShots = false;  // Ensure the shots are reset when a new player is selected
        });

      // Clear the player suggestions since we've selected a player
      this.playerSuggestions = [];
    }
  }



  onEnterPress(): void {
    if (this.playerSuggestions.length > 0) {
      // Select the first player in the suggestions
      const topSuggestion = this.playerSuggestions[0];

      // Update the search input with the full name of the top suggestion
      this.playerName = topSuggestion.name;

      // Proceed to select the player and fetch their summary
      this.onPlayerSelect(topSuggestion.id);
    } else {
      // If no suggestions, prompt the user to select from the list
      alert('Please select a player from the list.');
    }
  }


  searchPlayer(): void {
    if (this.playerSuggestions.length === 1) {
      this.onPlayerSelect(this.playerSuggestions[0].id);
    } else if (this.playerSuggestions.length > 1) {
      this.onPlayerSelect(this.playerSuggestions[0].id);
    } else {
      this.apiResponse = null;
      this.showShots = false;  // Reset shots if no valid player is found
      alert('No players found. Please refine your search.');
    }
  }


  highlight(player: any): void {
    // Implement any logic if necessary (like highlighting)
  }

  removeHighlight(player: any): void {
    // Logic for removing highlights
  }

  // Method to navigate to the previous game
  prevGame() {
    if (this.currentGameIndex > 0) {
      this.currentGameIndex--;
      this.showShots = false; // Reset shots view when switching games
    }
  }

  // Method to navigate to the next game
  nextGame() {
    if (this.currentGameIndex < this.apiResponse.games.length - 1) {
      this.currentGameIndex++;
      this.showShots = false; // Reset shots view when switching games
    }
  }

  // Method to view shots on the court
  viewShots() {
    this.showShots = true; // Show the shots when this method is called
  }

  getShotStyle(shot: any) {
    const courtWidth = 600; // Width of your court image in pixels
    const courtHeight = 470; // Height of your court image in pixels

    // Estimate of the actual court dimensions (in feet)
    const realCourtWidth = 44; // Real-world court width in feet (NBA regulation width)
    const realCourtHeight = 47; // Real-world court height in feet

    // Scaling factors to convert feet to pixels
    const scaleX = courtWidth / realCourtWidth;
    const scaleY = courtHeight / realCourtHeight;

    // The origin is now at the bottom center of the court
    let x = (shot.location_x + realCourtWidth / 2) * scaleX; // Shift X to start from the center
    let y = (shot.location_y) * scaleY; // Y increases upwards, no need to invert

    // Ensure shots don't go out of court (optional adjustments)
    if (x < 0) x = 0; // Prevent out of bounds on left side
    if (x > courtWidth) x = courtWidth; // Prevent out of bounds on right side
    if (y < 0) y = 0; // Prevent below-court placement
    if (y > courtHeight) y = courtHeight; // Prevent above-court placement


    return {
      left: `${x}px`, // Position on the X-axis (left-right)
      top: `${courtHeight - y}px`, // Position on the Y-axis, starting from the bottom
    };
  }


// Hide stats and shots when clearing data
  clearPlayerStats(): void {
    this.apiResponse = null;
    this.showShots = false; // Ensure shots are hidden when stats are hidden
  }

}
