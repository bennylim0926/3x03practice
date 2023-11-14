pipeline {
	agent any
	
	stages {
	// 	stage ('Checkout') {
	// 		steps {
	// 			git branch:'master', url: 'https://github.com/OWASP/Vulnerable-Web-Application.git' //to change
	// 		}
	// 	}
	// To build
	
	// OWASP
	stage('OWASP Dependency-Check Vulnerabilities') {
			steps {
				dependencyCheck additionalArguments: '--format HTML --format XML --suppression suppression.xml', odcInstallation: 'OWASP Dependency-Check Vulnerabilities'
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
	}
	// Automated Testing
	stage('Selenium Headless Test'){
		parallel {
                stage('Deploy') {
                    agent any
                    steps {
                        sh './deploy.sh'
						input message: 'Finished using the web site? (Click "Proceed" to continue)'
						sh './kill.sh'    
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
        }
	}
	post {		
		always {
			recordIssues enabledForFailure: true, tool: sonarQube()
		}
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		}
	}
}
