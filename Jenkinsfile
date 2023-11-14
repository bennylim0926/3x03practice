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
						sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=OWASP -Dsonar.sources=."
					}
				}
			}
		}
	}
	// Automated Testing
	post {		
		always {
			recordIssues enabledForFailure: true, tool: sonarQube()
		}
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		}
	}
}
