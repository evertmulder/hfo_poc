pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'hello'
      }
    }

    stage('test') {
      steps {
        sh 'ls -la'
      }
    }

    stage('deploy') {
      steps {
        sleep 2
        echo 'deploy'
      }
    }

  }
}
