const createWindowsInstaller = require('electron-winstaller').createWindowsInstaller
const path = require('path')

getInstallerConfig()
  .then(createWindowsInstaller)
  .catch((error) => {
    console.error(error.message || error)
    process.exit(1)
  })

function getInstallerConfig () {
  console.log('Creating windows installer')
  const rootPath = path.join('./')
  const outPath = path.join(rootPath, 'release-builds')

  return Promise.resolve({
    appDirectory: path.join(rootPath, 'Chives-win32-x64'),
    authors: 'Chives Network',
    version: process.env.CHIVES_INSTALLER_VERSION,
    noMsi: true,
    iconUrl: 'https://raw.githubusercontentHiveProject2021/chives-blockchain/master/electron-react/src/assets/img/chives.ico',
    outputDirectory: path.join(outPath, 'windows-installer'),
    certificateFile: 'win_code_sign_cert.p12',
    certificatePassword: process.env.WIN_CODE_SIGN_PASS,
    exe: 'Chives.exe',
    setupExe: 'ChivesSetup-' + process.env.CHIVES_INSTALLER_VERSION + '.exe',
    setupIcon: path.join(rootPath, 'src', 'assets', 'img', 'chives.ico')
  })
}
