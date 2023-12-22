# Code from: https://www.reddit.com/r/adventofcode/comments/189m3qw/2023_day_3_solutions/
# author: https://www.reddit.com/user/SavaloyStottie/
# language: PowerShell

$data = (Get-Content -Path "d03_input.txt").Split([System.Environment]::NewLine)

$sum = 0
$numbers = @()
$gears = @()

for ($i = 0; $i -lt $data.Count; $i++){
    $rownumbers = ([regex]::matches($data[$i],"(\d+)"))
    foreach ($number in $rownumbers) {
        $number | Add-Member -NotePropertyMembers @{Row=$i}
    }
    $numbers += $rownumbers

    $rowgears = ([regex]::matches($data[$i],"[*]"))
    foreach ($gear in $rowgears){
        $gear | Add-Member -NotePropertyMembers @{Row=$i}
    }
    $gears += $rowgears
}

    
foreach ($gear in $gears) {
    $gearnos = $numbers | Where-Object {$_.Row -In ($gear.Row-1)..($gear.Row+1) -and $gear.Index -In ($_.Index-1)..($_.Index + $_.Length)}
    if ($gearnos.Count -eq 2) { $sum += [Convert]::ToInt32($gearnos[0].Value) * [Convert]::ToInt32($gearnos[1].Value)}
}

$sum