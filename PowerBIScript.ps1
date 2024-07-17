# PowerShell script to publish a Power BI file to the Power BI service and perform data validation
# Install-Module -Name MicrosoftPowerBIMgmt -Force -AllowClobber
# Install-Module -Name dbatools -Force -AllowClobber

$workspaceId = "your_workspace_id"
$datasetName = "your_dataset_name"
$pbixFilePath = "C:\Users\Nishanti Dasari\Desktop\SEM 6 PRAC\Covid19DataAnalysis.pbix"

# Sign in to Power BI service
Connect-PowerBIServiceAccount

# Get the workspace
$workspace = Get-PowerBIWorkspace -Id $workspaceId

# Import the PBIX file to the workspace
Import-PowerBIFile -Path $pbixFilePath -WorkspaceId $workspace.Id -DatasetDisplayName $datasetName

# Trigger a dataset refresh
Invoke-PowerBIRestMethod -Url "groups/$($workspace.Id)/datasets/$datasetName/refreshes" -Method Post

# Sign out from Power BI service
Disconnect-PowerBIServiceAccount

# Data validation using dbatools (SQL Server module)
$serverInstance = "your_sql_server_instance"
$databaseName = "your_database_name"
$query = "SELECT * FROM your_table"

# Query the SQL Server database using dbatools
$queryResult = Invoke-Sqlcmd -ServerInstance $serverInstance -Database $databaseName -Query $query

# Compare the query result with the expected data
# Add your validation logic here

# Output the query result for further inspection
$queryResult

# Note: Ensure that you have the required permissions and securely handle sensitive information.
