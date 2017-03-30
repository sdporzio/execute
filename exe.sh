# Path to script directory
SCRIPTDIR="$(dirname "${BASH_SOURCE[0]}")"
# Check if input is file, if not, run as string
if [ -f "${1}" ]; then
  python ${SCRIPTDIR}/generateScript.py -if ${PWD}/${1}
else
  python ${SCRIPTDIR}/generateScript.py -is "${1}"
fi

source ${SCRIPTDIR}/script.tempexe
rm ${SCRIPTDIR}/script.tempexe
rm ${SCRIPTDIR}/Logs/*.templog
