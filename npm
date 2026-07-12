const { execSync } = require('child_process');
const semver = require('semver');

/**
 * Funkcija koja dohvata instaliranu verziju paketa iz lokalnog projekta
 * @param {string} packageName - Naziv paketa (npr. '@web3auth/base')
 * @returns {string|null} - Verzija paketa ili null ako paket nije instaliran
 */
function getInstalledVersion(packageName) {
    try {
        // Čita verziju direktno iz instaliranih node_modules radi preciznosti
        const packageJsonPath = require.resolve(`${packageName}/package.json`);
        const packageJson = require(packageJsonPath);
        return packageJson.version;
    } catch (error) {
        console.error(`❌ Greška: Paket ${packageName} nije pronađen u lokalnim zavisnostima.`);
        return null;
    }
}

/**
 * Funkcija koja preko npm registra dohvata najnoviju (latest) verziju paketa
 * @param {string} packageName - Naziv paketa
 * @returns {string|null} - Najnovija verzija sa npm-a
 */
function getLatestNpmVersion(packageName) {
    try {
        // Izvršava sinhronu shell komandu za povlačenje informacija sa npm-a
        const stdout = execSync(`npm view ${packageName} version`, { stdio: ['pipe', 'pipe', 'ignore'] });
        return stdout.toString().trim();
    } catch (error) {
        console.error(`❌ Greška pri komunikaciji sa npm registrom za paket ${packageName}.`);
        return null;
    }
}

/**
 * Glavna funkcija za automatsku proveru verzije i detekciju ispeglanih bagova
 * @param {string} packageName - Naziv Web3Auth paketa koji se proverava
 */
async function autoCheckWeb3AuthVersion(packageName = '@web3auth/base') {
    console.log(`🔍 Pokrećem automatsku proveru verzije za: ${packageName}...\n`);

    const currentVersion = getInstalledVersion(packageName);
    if (!currentVersion) return;

    const latestVersion = getLatestNpmVersion(packageName);
    if (!latestVersion) return;

    console.log(`📊 Trenutna instalirana verzija: ${currentVersion}`);
    console.log(`🚀 Najnovija dostupna verzija:    ${latestVersion}`);

    // Poređenje verzija pomoću semver biblioteke
    if (semver.gt(latestVersion, currentVersion)) {
        console.log('\n==================================================');
        console.log(`⚠️  UPOZORENJE: Izašla je nova verzija (${latestVersion})!`);
        console.log(`   Moguće je da je bag koji te muči ispeglan u novijoj verziji.`);
        console.log(`   Pokreni sledeću komandu za ažuriranje:`);
        console.log(`   👉 npm install ${packageName}@latest`);
        console.log('==================================================\n');
        
        // Ovde možeš dodati logiku da skripta baci grešku (throw) ako želiš da zaustaviš CI/CD proces
    } else {
        console.log('\n✅ Koristiš najnoviju verziju Web3Auth SDK-a. Ako bag i dalje postoji, verovatno još nije rešen.');
    }
}

// Pokretanje skripte (možeš promeniti naziv paketa po potrebi, npr. '@web3auth/modal')
autoCheckWeb3AuthVersion('@web3auth/base');
