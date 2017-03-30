# Path to script directory
SCRIPTDIR=$(dirname "${BASH_SOURCE[0]}")
TIMESTAMP=$(date +%s)

mkdir ${SCRIPTDIR}/Logs/${TIMESTAMP}
mkdir ${SCRIPTDIR}/Scripts/${TIMESTAMP}
# Check if input is file, if not, run as string
if [ -f "${1}" ]; then
  python ${SCRIPTDIR}/generateScript.py -if ${PWD}/${1} -t ${TIMESTAMP}
else
  python ${SCRIPTDIR}/generateScript.py -is "${1}" -t ${TIMESTAMP}
fi

source ${SCRIPTDIR}/Scripts/${TIMESTAMP}/script.tempexe
rm -rf ${SCRIPTDIR}/Scripts/${TIMESTAMP}
rm -r ${SCRIPTDIR}/Logs/${TIMESTAMP}
