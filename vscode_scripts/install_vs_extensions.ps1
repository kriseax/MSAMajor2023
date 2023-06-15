#################################
########## Functions ############
#################################

function InstallEXE{
	param([string]$setupFile, [string]$argList)

    #### Call the EXE with the working directory of this script's location, pass it the argument list, and wait until the process completes
	$InstallResults = Start-Process -WorkingDirectory $PSScriptRoot -FilePath $setupFile -ArgumentList $argList -Wait -PassThru
	return $InstallResults
}

function InstallMSI{
	param([string]$msiFile, [string]$argList) 
    
    #### Call msiexec with the working directory of this script's location, pass it the argument list, and wait until the process completes
	$InstallResults = Start-Process msiexec -WorkingDirectory $PSScriptRoot -ArgumentList $argList -Wait -PassThru
	return $InstallResults
}

function InstallWIM{
	param([string]$setupFile, [string]$argList, [string]$wimFile) 
    $fileExt = [IO.Path]::GetExtension($setupFile)
    $mountPath = "$PSScriptRoot\mount"
    if($fileExt -eq ".msi") {

        if(Test-Path -Path $mountPath){Dismount-WindowsImage -Path $mountPath -Discard}else{New-Item -Path $mountPath -ItemType Directory}
        # Mount the specified WIM in the specified mount directory
        Mount-WindowsImage -ImagePath "$PSScriptRoot\$wimFile" -Index 1 -Path $mountPath
        $InstallResults = InstallMSI $mountPath\$setupFile $argsList

    }
    else {

        if(Test-Path -Path $mountPath){Dismount-WindowsImage -Path $mountPath -Discard}else{New-Item -Path $mountPath -ItemType Directory}
        # Mount the specified WIM in the specified mount directory
        Mount-WindowsImage -ImagePath "$PSScriptRoot\$wimFile" -Index 1 -Path $mountPath
        $InstallResults = InstallEXE $mountPath\$setupFile $argsList

    }
    # Dismount the $mountPath
    Dismount-WindowsImage -Path $mountPath -Discard
	return $InstallResults
}

function ListInstalledSoftware{

    # Prevents script from stopping if some entries in registry don't have DisplayName/DisplayVersion
    $ErrorActionPreference = "SilentlyContinue"
    # Retrieves the information under 32/64-bit registry uninstall folders, expands and selects the property for DisplayName,UninstallString
    # Targeting these fields prevents corrupt registry entries from failing the script
    $InstalledSoftware = Get-ChildItem -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall, HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall | Get-ItemProperty -Name DisplayName,DisplayVersion,UninstallString | Select-Object DisplayName,DisplayVersion,UninstallString
    $InstalledSoftware | sort DisplayName | Out-GridView

}

function ApplicationDetectionMethod{
    # Enter display name and use * for wildcards
    $applicationName = "Microsoft Visual Studio Code"
    # Version as displayed in registry which may be slightly different than it appears elsewhere
    $ApplicationVersion = "1.57.1"
    # Prevents script from stopping if some entries in registry don't have DisplayName/DisplayVersion
    $ErrorActionPreference = "SilentlyContinue"
    # Retrieves the information under 32/64-bit registry uninstall folders, expands the property for DisplayName/DisplayVersion, selects only DisplayName/DisplayVersion (targeting these fields prevents corrupt registry entries from failing the script)
    $InstalledSoftware = Get-ChildItem -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall, HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall | Get-ItemProperty -Name DisplayName,DisplayVersion | Select-Object DisplayName,DisplayVersion
    $Detection = $InstalledSoftware | Where-Object {($_.DisplayName -like $ApplicationName) -and ([Version]$_.DisplayVersion -ge [Version]$ApplicationVersion) }
    if ($Detection) { Write-Output "Installed" }
    else { }
}

if($null -eq $args[0]) {

	#### Install VS Code Extensions ####
	code --install-extension ms-python.python
	code --install-extension ms-toolsai.jupyter
	code --install-extension mechatroner.rainbow-csv
	
    #### If $Results isn't empty exit with its exit code
    if($null -ne $Results) { $host.SetShouldExit($Results.ExitCode) }

}
else {
    switch ($args[0]) { 
        ListInstalledSoftware {ListInstalledSoftware}
        ApplicationDetectionMethod {ApplicationDetectionMethod}
    }
}


