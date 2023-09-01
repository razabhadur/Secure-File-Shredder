# Enhanced Secure File Shredder

The Enhanced Secure File Shredder is a sophisticated tool designed to ensure that deleted files remain unrecoverable. In the digital realm, merely deleting a file doesn't guarantee its removal from the storage medium. This tool addresses this security concern by overwriting the file multiple times with random data before deletion, making it nearly impossible to recover.

## Features

- **File Selection**: Enables users to select specific files for secure deletion.
- **Multiple Overwrite Passes**: Overwrites the file multiple times with random data, ensuring its unrecoverability.
- **Deletion Verification**: Confirms that the file content has been changed before deletion.
- **Logging**: Maintains a detailed log of securely deleted files for user reference.
- **User Interface**: Offers a streamlined command-line interface for easy user interaction.

## Usage

1. Clone the repository or download the script.
2. Run the script:
   ```
   python enhanced_secure_file_shredder.py
   ```
3. Input the path of the file you wish to securely delete.
4. Specify the number of overwrite passes (default is 3).
5. Review the log for confirmation of secure deletion.

## Contributing

Contributions are always welcome! Please submit a pull request or open an issue to suggest improvements or add new features.

## License

This project is licensed under the MIT License.

## Disclaimer

This tool is for educational and informational purposes only. Ensure thorough testing before using in any critical or production environments.
