<#
.SYNOPSIS
    Get all registered computers from Canonical Landscape
.DESCRIPTION
    Get a list of computers associated with the account used for authentication.
.PARAMETER LandscapeAPI
    Landscape API endpoint. Defaults to https://landscape.canonical.com/api
.PARAMETER Key
    Landscape Access Key
.PARAMETER Secret
    Landscape Secret Key
.EXAMPLE
    Get-LSComputers -Secret <Secret> -Key <Key> | Format-Table

    Gets all computers from Landscape in a table format.
#>
function Get-LSComputers {

    [CmdletBinding()]
    param (
        [string]$LandscapeAPI = "https://landscape.canonical.com/api",
        [Parameter(Mandatory, HelpMessage="Landscape Access Key")]
        [string]$Key,
        [Parameter(Mandatory, HelpMessage="Landscape Secret Key")]
        [string]$Secret
        
    )

    $Action = "GetComputers"

    $LandscapeAPI -match 'https?://(.*)/(.*)' >$null
    $Domain = $Matches[1]
    $Path = $Matches[2]

    Add-Type -AssemblyName System.Web
    $Timestamp = (Get-Date (Get-Date).ToUniversalTime() -Format s) + 'Z'
    $TimestampEncoded = [System.Web.HTTPUtility]::UrlEncode($Timestamp)
    $TimestampEncoded = [string]$TimestampEncoded.ToUpper()

    $Message = "GET`n$Domain`n/$Path/`n"
    $Params = "access_key_id=$($Key)&action=$($Action)&signature_method=HmacSHA256&signature_version=2&timestamp=$($TimestampEncoded)&version=2011-08-01"
    $Message = $Message + $Params

    # Signature
    $Hmacsha = New-Object System.Security.Cryptography.HMACSHA256
    $Hmacsha.key = [Text.Encoding]::UTF8.GetBytes($Secret)
    $Hash = $Hmacsha.ComputeHash([Text.Encoding]::UTF8.GetBytes($Message))  
    $Base64Hash = [Convert]::ToBase64String($Hash)
    $EncodedBase64Hash = [System.Web.HTTPUtility]::UrlEncode($Base64Hash)
        
    $URI = $LandscapeAPI + "/?" + $Params + "&signature=$($EncodedBase64Hash)"
    
    Return Invoke-RestMethod -Method Get -Uri $URI -UseBasicParsing   
}