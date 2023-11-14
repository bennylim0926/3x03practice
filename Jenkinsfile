pipeline {
	agent any
	stages {
		// OWASP
		stage('OWASP Dependency-Check Vulnerabilities') {
			steps {
        dependencyCheck additionalArguments: ''' 
                    -o './'
                    -s './'
                    -f 'ALL' 
                    --prettyPrint''', odcInstallation: 'OWASP Dependency-Check Vulnerabilities'
        
        dependencyCheckPublisher pattern: 'dependency-check-report.xml'
      }
		}
		// SonarQube
		stage('Code Quality Check via SonarQube') {
			steps {
				script {
					def scannerHome = tool 'SonarQube';
					withSonarQubeEnv('SonarQube') {
						sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=3x03 -Dsonar.sources=."
					}
				}
			}
		}
		stage('Deploy') {
				agent any
				steps {
					sh './deploy.sh'
					input message: 'Finished using the web site? (Click "Proceed" to continue)'
					
				}
		}
		stage('Selenium Tests') {
				agent {
					docker {
						image 'infologistix/docker-selenium-python' // or another image with Selenium and required browsers/drivers
						args '-v .:/tests --network host' // Mount the tests directory
					}
				}
				steps {
					sh 'python ui_selenium_test.py' // Run the Selenium tests
				}
			}				
	}
	post{
		success {
			recordIssues enabledForFailure: true, tool: sonarQube()
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
			sh './kill.sh'    
		}
	}
	
}
