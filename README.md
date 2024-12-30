# AdblockList-DNS Project

## Overview
The AdblockList-DNS project provides additive DNS sinkhole lists for blocking unwanted domains, such as advertisements and threats. The goal is to maintain and distribute these lists to enhance network security and user experience by filtering out undesired traffic at the DNS level.

This project is maintained by **FNI** and focuses on two primary use cases:

1. **Ads List**: Designed to block advertisement domains, improving user experience by preventing intrusive ads. 
2. **Threats List**: Used to block malicious or suspicious domains, supplementing existing FortiGate security mechanisms.

The primary emphasis is on maintaining and curating the ads list, while the threats list is secondary, as FortiGate handles much of this by default. The ads list may be split into multiple sublists for easier management and deployment.

---

## Features
- **Additive DNS Sinkhole Lists**: Easily extend DNS filtering capabilities.
- **Customizable**: Separate lists for ads and threats.
- **Regular Updates**: Ensures the lists stay effective and relevant.
- **Compatible with STIX Format**: For use with FortiGate and other platforms requiring structured threat feeds.

---

## Getting Started

### Prerequisites
To use these DNS sinkhole lists, ensure you have:
- A DNS server capable of importing custom block lists.
- Access to FortiGate or other compatible security appliances for threat feed integration.
- Python 3.x (for generating STIX-formatted lists, if needed).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Grunaura/AdblockList-DNS.git
   cd AdblockList-DNS
   ```

2. Use the provided block lists in your DNS server configuration. The lists are located in the `lists/` directory.

3. For FortiGate integration, convert the lists to STIX format using the provided Python script (if applicable).

---

## Usage

### For Ads List
1. Import the ads block list into your DNS server.
2. Regularly update the list from this repository to keep it current.
3. If necessary, split the ads list into smaller segments for administrative purposes.

### For Threats List
1. Import the threats block list into your FortiGate or DNS server.
2. Use it as an additive feed to FortiGate's built-in threat filtering.

### Generating STIX Format
To convert the block lists into STIX format for FortiGate, use the included Python script. For example:

```bash
python3 convert_to_stix.py --input lists/ad_list.txt --output stix/ad_list.json
```

---

## File Structure
```
AdblockList-DNS/
├── lists/
│   ├── ad_list.txt        # Block list for ads
│   ├── threats_list.txt   # Block list for threats
├── scripts/
│   ├── convert_to_stix.py # Script to convert block lists to STIX format
├── README.md              # Project documentation
```

---

## Contribution
We welcome contributions to improve the block lists or add new functionality. To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with your changes.

---

## License
This project is licensed under the [Creative Commons Zero v1.0 Universal (CC0 1.0)](https://creativecommons.org/publicdomain/zero/1.0/). You are free to use, modify, and distribute this work without restriction.

---

## Maintainers
**FNI Team**

---

## Future Plans
- Automate the splitting of ads lists into smaller segments.
- Regular integration of third-party block lists.
- Improved threat list curation.
- Comprehensive testing and validation workflows.
